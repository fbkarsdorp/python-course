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
        results.fragmenter.maxchars = 300
        results.fragmenter.surround = 50
        for hit in results:
            result = dict(hit)
            with open(result['path']) as infile:
                result['snippet'] = hit.highlights("text", infile.read(), top=3)
            yield result


def to_html(result):
    "Return a representation of a search result in HTML."
    title = result['title'] if 'title' in result else result['id']
    author = result['author'] if 'author' in result else ''
    html = """<div id='match'>
                 <span id='id'>
                    <a href='%s' target='_blank'>%s</a>
                 </span>
                 </br>
                 <span id='author'>%s</span>
                 </br>
                 <span id='text'>%s</span>
              </div>
           """ % (result['source'], title, author, result['snippet'])
    return html


app = Flask(__name__)

@app.route('/searchbox', methods=['GET', 'POST'])
def searchbox():
    query = request.form['q'].strip()
    html_results = '\n'.join(map(to_html, search(query)))
    return jsonify({'html': html_results})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000, use_reloader=True, threaded=True)
