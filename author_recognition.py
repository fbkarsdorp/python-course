#! /usr/bin/env python3
# -*- coding: utf8 -*-

import os
import sys

from collections import defaultdict
from math import log

from preprocess import tokenise, readcorpusfile


def predict_author(text):
    "Predict the author of 'text' on the basis of the feature_database."
    return classify(score(extract_features(text)))

def classify(scores):
    "Return the author with the highest probability."
    return max(scores, key=scores.__getitem__)

def extract_features(filename):
    "Open and tokenise the contents of a file."
    return tokenise(open(filename, encoding="latin-1").read())

def extract_author(filename):
    "Extract the name of the author from the filename."
    return filename.split('/')[-1].split('-')[0]

def update_counts(author, text, feature_database):
    "Update the counts for this author, text pair in the database."
    for feature in text:
        feature_database[author][feature] += 1
    return feature_database

def add_file_to_corpus(filename, feature_database):
    "Add a text (which is a list of sentences) to the corpus."
    return update_counts(extract_author(filename), 
                         extract_features(filename),
                         feature_database)

def add_dir_to_corpus(directory, feature_database):
    "Add all files from a directory to the corpus."
    for filename in os.listdir(directory):
        feature_database = add_file_to_corpus(
            os.path.join(directory, filename), feature_database)
    return feature_database

def log_probability(feature_counts, features_sum, n_features):
    return log((feature_counts + 1.0) / (features_sum + n_features))

def init_score_function(feature_database):
    n_features = len(set(feature for author, features in feature_database.items() 
                                 for feature in features))
    def score(document):
        "Predict who wrote the document on the basis of the corpus."
        scores = defaultdict(float)
        for author in feature_database:
            features_sum = sum(feature_database[author].values())
            for feature in document:
                scores[author] += log_probability(
                    feature_database[author][feature], features_sum, n_features)
        return scores
    return score

def test_from_corpus(directory, feature_database):
    "Predict the authors for all files in the directory."
    results = []
    for filename in os.listdir(directory):
        features = extract_features(os.path.join(directory, filename))
        author = extract_author(filename)
        prediction = predict_author(features, feature_database)
        results.append((author, prediction))
    return results

def analyze_results(results):
    "Return the fraction of correct predictions."
    correct = 0.0
    for author, prediction in results:
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
                    
    #Verify that the corpus directory exists        
    if not os.path.exists(traincorpusdirectory):
        print("The specified training corpus does not exist")
        sys.exit(1)  
        
    #Verify that the test document exists    
    if not os.path.exists(testdocument):
        print("The specified test document does not exist")
        sys.exit(1)      


    feature_database = defaultdict(lambda: defaultdict(int))
    feature_database = add_dir_to_corpus(traincorpusdirectory, feature_database)
    score = init_score_function(feature_database)
    if os.path.isdir(testdocument):
        for filename in os.listdir(testdocument):
            print(predict_author(os.path.join(testdocument, filename)))
    else:
        print(predict_author(testdocument))
