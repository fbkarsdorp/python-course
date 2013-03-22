#! /usr/bin/env python3
# -*- coding: utf8 -*-
import os
import sys

from collections import defaultdict
from math import log
from string import punctuation as PUNCTUATION
from glob import glob

def predict_author(document, corpus):
    "Predict who wrote the document on the basis of the corpus."
    scores = defaultdict(float)
    # get the number of unique features used in the training corpus
    n_features = len(set(feature for author, features in corpus.items() 
                                 for feature in features))
    for author in corpus:
        # this is normally for class prior smoothing.
        #scores[author] += log(author_counts[author] / sum(author_counts.values()))
        author_feature_sum = sum(corpus[author].values())
        for feature in document:
            scores[author] += log((corpus[author][feature] + 1.0) / 
                                  (author_feature_sum + n_features))
    return max(scores, key=scores.__getitem__)

def get_author(filename):
    return filename.split('-')[0]

def add_file_to_corpus(text, author, corpus):
    "Add a text (which is a list of sentences) to the corpus."
    # text is a list of sentences
#    author = filename.split('-')[0]
    tokens = tokenise(text)
    sentences = splitsentences(tokens)
    for sentence in sentences:
        for word in sentence:
            corpus[author][word] += 1
    return corpus

def add_dir_to_corpus(directory, corpus):
    "Add all files from a directory to the corpus."
    for filename in os.listdir(directory):
        corpus = add_file_to_corpus(
            readcorpusfile(os.path.join(directory, filename)), 
            get_author(filename), corpus)
    return corpus

def test_from_corpus(directory, corpus):
    "Predict the authors for all files in the directory."
    results = []
    for filename in os.listdir(directory):
        text = tokenise(readcorpusfile(os.path.join(directory, filename)))
        author = get_author(filename)
        prediction = predict_author(text, corpus)
        results.append((filename, author, prediction))
    return results



WHITESPACE = [" ", "\t", "\n", "\r", "\f", "\v"]

def readcorpusfile(filepath, encoding='latin-1'):
    f = open(filepath,'rt', encoding=encoding)
    text = f.read()
    f.close()
    return text
          
def tokenise(text):
    tokens = []
    begin = 0
    for i, c in enumerate(text):
        if c in PUNCTUATION or c in WHITESPACE:
            token = text[begin:i]
            tokens.append(token)
            if c not in WHITESPACE:
                tokens.append(c) #anything but spaces and newlines (i.e. punctuation) counts as a token too
            begin = i + 1 #set the begin cursor
    return tokens
            
def is_end_of_sentence(i, tokens):
    # is this an end-of-sentence marker? ... and is this either 
    # the last token or the next token is NOT an end of sentence 
    # marker as well? (to deal with ellipsis etc, bonus)
    return tokens[i] in ('.','?','!') and (i == len(tokens) - 1 or not tokens[i+1] in ('.','?','!'))

def splitsentences(tokens):
    sentences = []
    begin = 0
    for i, token in enumerate(tokens):
        if is_end_of_sentence(i, tokens): 
            sentences.append( tokens[begin:i+1] )
            begin = i+1
    return sentences
            
def getngrams(sentence, n):   
    if n == 1: 
        return sentence
    ngrams = []
    for begin in range(0, len(sentence) - n + 1):
        ngrams.append( sentence[begin:begin+n] )
    return ngrams
           
def makefrequencylist(sentences, n=1):    
    freqlist = defaultdict(int)
    for sentence in sentences:
        for ngram in getngrams(sentence,n):
           freqlist[ngram] += 1
    return freqlist

try:
    traincorpusdirectory = sys.argv[1]
    testdocument = sys.argv[2]
except: 
    print("Specify the directory of the training corpus as the first argument to the program")
    print("Specify the text you want to analyse as the second argument")
    print("Specify the n-gram order to use as third argument")
    sys.exit(1)
    
try:
    n = int(sys.argv[3])
except IndexError: 
    #No value specified, let's just choose 1 and continue
    n = 1
except ValueError:
    print("n must be a number!")
        
#Verify that the corpus directory exists        
if not os.path.exists(traincorpusdirectory):
    print("The specified training corpus does not exist")
    sys.exit(1)  
    
#Verify that the test document exists    
if not os.path.exists(testdocument):
    print("The specified test document does not exist")
    sys.exit(1)      

corpus = {}
for filepath in glob(traincorpusdirectory + "/*.txt"):
    filename = os.path.basename(filepath)
    author = filename.split('-')[0] #the filename without the .txt extension is the author's name
    text = readcorpusfile(filepath)
    tokens = tokenise(text)
    sentences = splitsentences(tokens)
    # this will overwrite earlier assignments....
    corpus[author] = makefrequencylist(sentences,n)
print(predict_author(tokenise(readcorpusfile(testdocument)), corpus))

