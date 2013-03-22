#! /usr/bin/env python
# -*- coding: utf8 -*-

from preprocess import readcorpusfile, splitsentences, tokenise
from glob import glob
import sys
import os

def getleftcontext(tokens, i, contextsize):
    begin = i - contextsize
    if begin < 0: begin = 0 #begin musn't be negative (because that is special syntax for specifying an index from the right)
    return tokens[begin:i]
    
def getrightcontext(tokens, i, contextsize):
    return tokens[i+1:i+1+contextsize] #no problem if i+1+contextsize exceeds the len(tokens), but there will simply not be more to slice off 

if __name__ == '__main__':

    try:
        corpusdirectory = sys.argv[1]
        searchword = sys.argv[2]
    except: 
        print("Specify the directory of the corpus as the first argument to the program")
        print("Specify the word to look for as second argument to the program")
        print("Specify the context size as third argument to the program")
        sys.exit(1)
        
    try:
        contextsize = int(sys.argv[3])
    except IndexError:
        contextsize = 1
    except ValueError:
        print("Context size must be an integer")
    
    #Verify that the corpus directory exists        
    if not os.path.exists(corpusdirectory):
        print("The specified corpus does not exist")
        sys.exit(1)  
        
    corpus = {}
    for filepath in glob(corpusdirectory + "/*.txt"):
        filename = os.path.basename(filepath)
        author = filename.split('-')[0] #the part of the filename before the hyphen is the author's name
        text = readcorpusfile(filepath)
        tokens = tokenise(text)
        sentences = splitsentences(tokens)
        for sentence in sentences:
            for i, token in enumerate(tokens): 
                if token == searchword:
                    leftcontext = " ".join(getleftcontext(tokens,i,contextsize))
                    rightcontext = " ".join(getrightcontext(tokens,i,contextsize))
                    print leftcontext + " *" + token + "* " + rightcontext
                
