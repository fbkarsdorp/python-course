
from collections import defaultdict
from math import log


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


    
    
    
        
            
            
            
        
        
    
    
