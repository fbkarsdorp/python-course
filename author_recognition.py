#! /usr/bin/env python3
# -*- coding: utf8 -*-

from collections import defaultdict
from math import log
import sys
import os


def predict_author(document, corpus):
    scores = defaultdict(float)
    n_features = len(set(feature for author, features in corpus.items() 
                                 for feature in features))
    for author in corpus:
        #scores[author] += log(author_counts[author] / sum(author_counts.values()))
        author_n = sum(corpus[author].values())
        for feature in document:
            scores[author] += log((corpus[author][feature] + 1.0) / 
                                  (author_n + n_features))
    return max(scores, key=scores.__getitem__)

def readcorpusfile(filepath):
    f = open(filepath,'rt',encoding='utf-8')
    text = f.read()
    f.close()
    return text
          
def tokenise(text):
    tokens = []
    begin = 0
    for i, c in enumerate(text):
        if c in ("\n"," ",".","?","!",",",":",";","/","(",")","[","]","{","}","<",">","\"","'"):
            token = text[begin:i]
            tokens.append(token)
            if c != " " and c != "\n":
                tokens.append(c) #anything but spaces and newlines (i.e. punctuation) counts as a token too
            begin = i+1 #set the begin cursor
    return tokens
            

def splitsentences(tokens):
    sentences = []
    begin = 0
    for i, token in enumerate(tokens):
        #is this an end-of-sentence marker? ... and is this either the last token or the next token is NOT an end of sentence marker as well? (to deal with ellipsis etc, bonus)
        if token in ('.','?','!')      and (i == len(tokens) - 1 or not tokens[i+1] in ('.','?','!')): 
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
    freqlist = defaultdict(lambda: defaultdict(int))
    for sentence in sentences:
        for ngram in getngrams(sentence,n):
           freqlist[ngram] += 1
    return freqlist

try:
    traincorpusdirectory = sys.argv[1]
    testdocument = sys.argv[2]
except: 
    print "Specify the directory of the training corpus as the first argument to the program"
    print "Specify the text you want to analyse as the second argument"
    print "Specify the n-gram order to use as third argument"
    sys.exit(1)
    
try:
    n = int(sys.argv[3])
except IndexError: 
    #No value specified, let's just choose 1 and continue
    n = 1
except ValueError:
    print "n must be a number!"
        
#Verify that the corpus directory exists        
if not os.path.exists(traincorpusdirectory):
    print "The specified training corpus does not exist"
    sys.exit(1)  
    
#Verify that the test document exists    
if not os.path.exists(testdocument):
    print "The specified test document does not exist"
    sys.exit(1)      

corpus = {}
for root, dirs, files in os.walk(traincorpusdirectory):
    for filename in files:
        author = filename[:-4] #the filename without the .txt extension is the author's name
        filepath = os.path.join(root,filename)
        text = readcorpusfile(filepath)
        tokens = tokenise(text)
        sentences = splitsentences(tokens)
        corpus[author] = makefrequencylist(sentences,n) 

