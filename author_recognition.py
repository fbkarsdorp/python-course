
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


def readcorpusfile(filename):
    f = open(filename,'rt',encoding='utf-8')
    text = f.read()
    f.close()
    return text

          
def tokenizer(text,separatorlist, abbreviationlist):
    tokens = []
    begin = 0
    for i, c in enumerate(text):
        if c in separatorlist:
            token = text[begin:i]
            if c == '.' and token in abbreviationlist:
                #this is an abbreviation ending in a period, do not split the period
                tokens.append(token + c) 
            elif (c == '.' or c == ',') and token.isdigit() and (i < len(tokens) - 1 and tokens[i+1].isdigit()):
                #period is probably a decimal or thousands separator, let's keep these together and just continue with the next
                continue
            elif c != " " and c != "\n": 
                tokens.append(token)
                tokens.append(c) #anything but spaces and newlines (i.e. punctuation) counts as a token too
            begin = i+1 #set the begin cursor
    return tokens
            
            

def getsentences(tokens):
    sentences = []
    begin = 0
    for i, token in enumerate(tokens):
        #is this an end-of-sentence marker? ... and is this either the last token or the next token is NOT an end of sentence marker as well? (to deal with ellipsis etc)
        if token in ('.','?','!')      and (i == len(tokens) - 1 or not tokens[i+1] in ('.','?','!')): 
            sentences.append( tokens[begin:i+1] )
            begin = i+1
    return sentences
            
def getngrams(sentence, n):   
    ngrams = []
    for begin in range(0, len(sentence) - n + 1):
        ngrams.append( sentence[begin:begin+n] )
    return ngrams
       
    
        
            
            
            
        
        
    
    
