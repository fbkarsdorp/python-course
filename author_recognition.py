
from collections import defaultdict
from math import log

def train(corpus):
    feature_author_counts = {}
    feature_counts = defaultdict(int)
    for author, features in corpus.items():
        feature_author_counts[author] = features
        for feature, count in features.items():
            feature_counts[feature] = count
    return feature_counts, feature_author_counts

def test(document, feature_counts, feature_author_counts):
    scores = defaultdict(float)
    for feature in document:
        for author in feature_author_counts:
            scores[author] += log(
                (feature_author_counts[author][feature] + 1.0) / 
                (feature_counts[feature] + len(feature_counts)))
    return max(scores, key=scores.__getitem__)

