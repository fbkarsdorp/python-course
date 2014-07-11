import configparser
import glob
import os
import shutil
import subprocess
import sys

from os.path import splitext, basename

from whoosh.fields import Schema
from whoosh.fields import ID, KEYWORD, TEXT
from whoosh.index import create_in, open_dir

from bs4 import BeautifulSoup


pdf_schema = Schema(id = ID(unique=True, stored=True),
                    path = ID(stored=True),
                    source = ID(stored=True),
                    author = TEXT(stored=True),
                    title = TEXT(stored=True),
                    text = TEXT)


def fileid(filepath):
    """
    Return the basename of a file without its extension.
    >>> fileid('/some/path/to/a/file.pdf')
    file
    """
    base, _ = splitext(basename(filepath))
    return base


def parse_html(filename):
    """Extract the Author, Title and Text from a HTML file
    which was produced by pdftotext with the option -htmlmeta."""
    with open(filename) as infile:
        html = BeautifulSoup(infile, "html.parser", from_encoding='utf-8')
        d = {'text': html.pre.text}
        if html.title is not None:
            d['title'] = html.title.text
        for meta in html.findAll('meta'):
            try:
                if meta['name'] in ('Author', 'Title'):
                    d[meta['name'].lower()] = meta['content']
            except KeyError:
                continue
        return d


def pdftotext(pdf, outdir='.', sourcedir='source', p2t='pdftotext', move=False):
    """Convert a pdf to a text file. Extract the Author and Title
    and return a dictionary consisting of the author, title, text
    the source path, the path of the converted text file and the
    file ID."""
    filename = fileid(pdf)
    htmlpath = os.path.join(outdir, filename + '.html')
    txtpath = os.path.join(outdir, filename + '.txt')
    sourcepath = os.path.join(sourcedir, filename + '.pdf')
    subprocess.call([p2t, '-enc', 'UTF-8', '-htmlmeta', pdf, htmlpath])
    data = parse_html(htmlpath)
    os.remove(htmlpath)
    file_action = shutil.move if move else shutil.copy
    file_action(pdf, sourcepath)
    with open(txtpath, 'w') as outfile:
        outfile.write(data['text'])
    data['source'] = sourcepath
    data['path'] = txtpath
    data['id'] = fileid(pdf)
    return data


def index_collection(configpath):
    "Main routine to index a collection of PDFs using Whoosh."
    config = configparser.ConfigParser()
    config.read(configpath)
    recompile = config.getboolean("indexer.options", "recompile")
    # check whether the supplied index directory already exists
    if not os.path.exists(config.get("filepaths", "index directory")):
        # if not, create a new directory and initialize the index
        os.mkdir(config.get("filepaths", "index directory"))
        index = create_in(config.get("filepaths", "index directory"), schema=pdf_schema)
        recompile = True
    # open a connection to the index
    index = open_dir(config.get("filepaths", "index directory"))
    # retrieve a set of all file IDs we already indexed
    indexed = set(map(fileid, os.listdir(config.get("filepaths", "txt directory"))))
    # initialize a IndexWriter object
    writer = index.writer()
    for directory in config.get("filepaths", "pdf directory").split(';'):
        for filepath in glob.glob(directory + "/*.pdf"):
            # poor man's solution to check whether we already indexed this pdf
            if fileid(filepath) not in indexed or recompile:
                try:
                    data = pdftotext(
                        filepath,
                        outdir=config.get("filepaths", "txt directory"),
                        sourcedir=config.get("filepaths", "source directory"),
                        p2t=config.get('programpaths', 'pdftotext'),
                        move=config.getboolean("indexer.options", "move pdfs"))
                    writer.add_document(**data)
                except (IOError, UnicodeDecodeError) as error:
                    print(error)
    # commit out changes
    writer.commit()

if __name__ == '__main__':
    index_collection(sys.argv[1])
