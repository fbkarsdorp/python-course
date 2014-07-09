import os
import subprocess

from whoosh.fields import Schema
from whoosh.fields import ID, KEYWORD, TEXT


pdf_schema = Schema(id = ID, 
                    path = ID(stored=True), 
                    source = ID(stored=True), 
                    author = KEYWORD, 
                    text = TEXT)
