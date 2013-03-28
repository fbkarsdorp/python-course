#! /usr/bin/env python3
# -*- coding: utf8 -*-

import sys
import preprocess


class Tweet():    
    def __init__(self, user, message, time):
        assert isinstance(user, TwitterUser)
        self.user = user
        self.message = message
        self.time = time
        

class TwitterUser():
    def __init__(self, name):
        self.name = name
        self.tweets = [] #This will be a list of all tweets 
        self.relations = {} #This will be a dictionary in which the keys are TwitterUser objects and the values are the weight of the relation (an integer) 
    
    def append(self, tweet):
        assert isinstance(tweet, Tweet)
        self.tweets.append(tweet)
        
    def __iter__(self):
        for tweet in self.tweets:
            yield tweet
    
    def __hash__(self):    
        #For an object to be usable as a dictionary key, it must have a hash method. Call the hash() function over something that uniquely defined this object
        #and thus can act as a key in a dictionary. In our case, the user name is good, as no two users will have the same name:          
        return hash(self.name)
    
    def computerelations(self, graph):
        for tweet in self:
            tokens = preprocess.tokenise(tweet.message)
            for token in tokens:
                #Does this token look like twitter's @recipient syntax ??
                if token and token[0] == '@': 
                    user = token[1:]
                    if user and user != self.name: #user must not be empty, and must not be the user itself
                        if user in self.relations:
                            #the user is already in our relations, strengthen the bond:
                            self.relations[user] += 1
                        elif user in graph:                        
                            #the user exists in the graph, we can add a relation!
                            self.relations[user] = 1
                        #if the user does not exist in the graph, no relations will be added
        
    def printrelations(self):
        for recipient, weight in self.relations.items():
            print(self.name + " -> " + recipient + " (" + str(weight) + ")")
 
    def gephioutput(self):
        for recipient, weight in self.relations.items():
            for i in range(0, weight):
                yield self.name + "," + recipient
 
        
class TwitterGraph():
    def __init__(self, corpusdirectory):        
        self.users = {} #initialisation of dictionary that will store all twitter users. They keys are the names, the values are TwitterUser objects.

        #Load the twitter corpus
        for filepath in preprocess.find_corpus_files(corpusdirectory): 
            text = preprocess.read_corpus_file(filepath)
            for line in text.split("\n"):
                try:
                    user, time, tweetmessage = line.split("\t", 3) #do a maximum of three splits
                except ValueError:
                    continue #we have an invalid line in our data, ignore it and continue the for loop
                    
                if not user in self.users:
                    #we have a new user, make a new TwitterUser instance and add it to the dictionary:
                    self.users[user] = TwitterUser(user)

                #Does this message contain a @, which indicated there may be @recipient syntax in the message 
                #Otherwise, we are not interested in the tweet and just ignore it
                if tweetmessage.find('@') != -1:
                    tweet = Tweet(self.users[user], tweetmessage,time)
                    self.users[user].append(tweet)

        #Compute relations between users
        for user in self:
            user.computerelations(self)
    
    def __contains__(self, user):
        return user in self.users
    
    def __iter__(self):
        for user in self.users.values():
            yield user

    def __getitem__(self, user):    
        return self.users[user]
            

twittergraph = TwitterGraph(sys.argv[1])
for twitteruser in twittergraph:
    twitteruser.printrelations()

f = open('gephigraph.csv','wt',encoding='utf-8')
for twitteruser in twittergraph:
    for line in twitteruser.gephioutput(): 
        f.write(line + "\n")
f.close()
