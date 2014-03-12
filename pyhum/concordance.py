#! /usr/bin/env python
# -*- coding: utf8 -*-

from preprocess import readcorpus
import sys
import os

def getleftcontext(tokens, i, contextsize):
    begin = i - contextsize
    if begin < 0: begin = 0 #begin musn't be negative (because that is special syntax for specifying an index from the right)
    return tokens[begin:i]
    
def getrightcontext(tokens, i, contextsize):
    return tokens[i+1:i+1+contextsize] #no problem if i+1+contextsize exceeds the len(tokens), but there will simply not be more to slice off 

def concordance(tokens, queryword, contextsize):
    for i, token in enumerate(tokens): 
        if token.lower() == queryword.lower():
            leftcontext = " ".join(getleftcontext(tokens,i,contextsize))
            rightcontext = " ".join(getrightcontext(tokens,i,contextsize))
            print leftcontext + " *" + token + "* " + rightcontext        


if __name__ == '__main__':

    try:
        corpusdirectory = sys.argv[1]
        queryword = sys.argv[2]
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
        
    for filename, sentences in readcorpus(corpusdirectory):
        for sentence in sentences:
            concordance(sentence, queryword, contextsize)
