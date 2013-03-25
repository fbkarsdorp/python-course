#! /usr/bin/env python3
# -*- coding: utf8 -*-

import os
import sys

from collections import defaultdict
from math import log
from preprocess import tokenise, splitsentences, readcorpusfile, readcorpus, makefrequencylist6

def predict_author(text, training_data):
    return classify(score(text, training_data))

def classify(scores):
    return max(scores, key=scores.__getitem__)

def score(document, corpus):
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
    return scores

def get_author(filename):
    return filename.split('-')[0]

def add_file_to_corpus(text, author, corpus):
    "Add a text (which is a list of sentences) to the corpus."
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

def analyze_results(results):
    "Return the fraction of correct predictions."
    correct = 0.0
    for _, author, prediction in results:
        if author == prediction:
            correct += 1
    return correct / len(results)


if __name__ == '__main__':

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
    for filename, sentences in readcorpus(traincorpusdirectory):
        author = get_author(filename)
        freqlist = makefrequencylist(sentences,n)  
        #add to corpus
        for wordtype, count in freqlist.items():
            corpus[author][wordtype] += count        
                  
    print(predict_author(tokenise(readcorpusfile(testdocument)), corpus))
