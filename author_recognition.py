
from collections import defaultdict
from math import log

def train(corpus):
    author_feature_counts = {}
    feature_counts = defaultdict(int)
    for author, features in corpus.iteritems():
        author_feature_counts[author] = features
        for feature, count in features.iteritems():
            feature_author_counts[feature][author] = count
    return feature_counts, feature_author_counts

def test(document, feature_counts, feature_author_counts):
    scores = defaultdict(float)
    for feature in document:
        for author in model:
            scores[author] += math.log(
                (feature_author_counts[feature][author] + 1.0) / 
                (feature_counts[feature] + len(feature_counts)))
    return max(scores, key=scores.__getitem__, reverse=True)