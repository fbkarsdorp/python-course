import configparser

from flask import Flask, request, jsonify, render_template

from whoosh.index import open_dir
from whoosh.qparser import QueryParser

config = configparser.ConfigParser()
config.read("pydf.ini")

def search(query):
    index = open_dir(config.get("filepaths", "index directory"))
    query = QueryParser("text", index.schema).parse(query)
    with index.searcher() as searcher:
        results = searcher.search(
            query, limit=config.getint("indexer.options", "search limit"), terms=True)
        html_out = ''
        results.fragmenter.maxchars = 300
        results.fragmenter.surround = 50
        for result in results:
            fileid = result['id']
            title = result['title'] if 'title' in result else ''
            author = result['author'] if 'author' in result else ''
            with open(result['path']) as infile:
                html_out += """<div id='match'>
                              <span id='id'>
                                 <a href='%s' target='_blank'>%s</a>
                              </span>
                              <span id='author'>%s</span>
                              </br>
                              <span id='text'>%s</span>
                           </div>
                        """ % (result['source'], title if title else fileid,
                               author, 
                               result.highlights("text", text=infile.read(), top=3))
        return html_out


app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def api():
    return jsonify({'html': search(request.form['q'].strip())})

@app.route('/')
def index():
    return render_template('index.html', title='PDF viewer')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000, use_reloader=True, threaded=True)