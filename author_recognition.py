#! /usr/bin/env python3
# -*- coding: utf8 -*-

import os

from collections import defaultdict
from math import log

from preprocess import tokenise, splitsentences, readcorpusfile


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


