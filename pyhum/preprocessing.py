import os
import string

def strip_punctuation(s):
    """Return the text without (hopefully...) any punctuation.
    >>> strip_punctuation('this.is?as!funny@word') == 'thisisasfunnyword'
    """
    return ''.join(ch for ch in s if ch not in string.punctuation)

def clean_text(text):
	"Lowercase and strip all punctuation from a text."
	return strip_punctuation(text.lower())

def read_file(filename):
    "Read the contents of FILENAME and return as a string."
    infile = open(filename) 
    contents = infile.read()
    infile.close()
    return contents

def list_textfiles(directory):
    "Return a list of filenames ending in '.txt' in DIRECTORY."
    textfiles = []
    for filename in listdir(directory):
        if filename.endswith(".txt"):
            textfiles.append(directory + "/" + filename)
    return textfiles

def split_sentences(text):
    "Split a text string into a list of sentences."
    sentences = []
    start = 0
    for end, character in enumerate(text):
        if end_of_sentence_marker(character):
            sentence = text[start: end + 1]
            sentences.append(sentence)
            start = end + 1
    return sentences

def tokenize(text):
	"Tokenize a text into a list of sentences each represented as a list of words."
	return [clean_text(sentence).split() for sentence in split_sentences(text)]

def read_corpus(directory):
	"Read and tokenize all files in DIRECTORY."
	corpus = []
	for filename in list_textfiles(directory):
		corpus.append(tokenize(read_file(filename)))
	return corpus