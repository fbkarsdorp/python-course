#! /usr/bin/env python3
# -*- coding: utf8 -*-

import os
from collections import defaultdict
from string import punctuation as PUNCTUATION
from glob import glob

WHITESPACE = [" ", "\t", "\n", "\r", "\f", "\v"]

def readcorpusfile(filepath, encoding='utf-8'):    
    """Returns the full raw text of the corpus document, in a single string"""
    f = open(filepath,'rt', encoding=encoding)
    text = f.read()
    f.close()
    return text

def findcorpusfiles(corpusdirectory):
    """Returns a list of all filenames of corpus files"""
    return glob(corpusdirectory + "/*.txt")      
          
def tokenise(text):
    """Tokenises a string and returns a list of tokens"""
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
    """Split sentences, returns sentences as a list of lists of tokens
     (each sentence is a list of tokens)"""
    sentences = []
    begin = 0
    for i, token in enumerate(tokens):
        if is_end_of_sentence(i, tokens): 
            sentences.append( tokens[begin:i+1] )
            begin = i+1
    return sentences
            
def getngrams(sentence, n):   
    """Extract n-grams from a sentence, where a sentence is a list of tokens"""
    if n == 1: 
        return sentence
    ngrams = []
    for begin in range(0, len(sentence) - n + 1):
        ngrams.append( sentence[begin:begin+n] )
    return ngrams
           
def makefrequencylist(sentences, n=1):    
    """Make a frequency list given sentences of a corpus file"""
    freqlist = defaultdict(int)
    for sentence in sentences:
        for ngram in getngrams(sentence,n):
           freqlist[ngram] += 1
    return freqlist

def readcorpus(corpusdirectory):
    """Read and preprocess corpus, will iterate over all corpus files 
    one by one, tokenise them, split sentences, and return/yield them """
    for filepath in findcorpusfiles(corpusdirectory):
        filename = os.path.basename(filepath)
        text = readcorpusfile(filepath)
        tokens = tokenise(text)
        sentences = splitsentences(tokens)
        yield filename, sentences
