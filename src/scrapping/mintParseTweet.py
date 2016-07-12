# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 12:21:51 2016

@author: jortilles
"""

import json
from pprint import pprint

class MintParseTweet:
    urlList = list()
    data = list()
    #def __init__(self):
       #self.readFile()
    
    
    def readFile(self):    
        with open('tweets.txt') as f:
            for line in f:
                self.data.append(json.loads(line))     
            f.close() 
        self.extractUrlsFromTweets()
    
    def list(self):
        pprint(self.data)    
    
    def parseString(self, my_string):
        try:
            tweet = json.loads(my_string)
            self.parseUrl(tweet)
            #print "processing .... ",  my_string            
            
        except:
            #print("Problem parsign tweet.... " )
            #print string
            print("Problem parsign tweet.... ")
        return self.urlList
            
    def parseUrl(self, tweet):
         #print tweet
         urls = tweet["entities"]["urls"]                 
         #print "urls presents in tweet ", urls
         for url in urls:
             print "appending ", url["expanded_url"]
             self.urlList.append(url["expanded_url"])
        
    def extractUrlsFromTweets(self):
        for tweet in self.data:
            self.parseUrl(tweet )
                    
                    
    def printUrls(self):
        for url in self.urlList:
            print url
        

    def getUrlList(self):
        return self.urlList