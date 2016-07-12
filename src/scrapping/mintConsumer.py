# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:06:27 2016

@author: jortilles
"""

from pykafka import KafkaClient
import json
from pprint import pprint

class MintConsumer:
    urlList = list()
    tweetList = list()
    def __init__(self  ):
        self.client = KafkaClient(hosts="127.0.0.1:9092,127.0.0.1:9093")
        self.topic = self.client.topics['unique_tweets']

#with topic.get_sync_producer() as producer:
#    for i in range(4):
#        producer.produce('test message ' + str(i ** 2))
        
    
    def consume(self):        
        self.consumer = self.topic.get_simple_consumer(consumer_timeout_ms=3000)
        for message in self.consumer:
            #print message.offset, message.value
            #print message.value            
            mp = MintParse() 
            messageArray = mp.parseString(message.value)
            for element in messageArray:
                self.urlList.append( element )
            #print self.urlList
        return self.urlList
 


    def getTweetsFromKafka(self):
        self.consumer = self.topic.get_simple_consumer(consumer_timeout_ms=3000)
        for message in self.consumer:
           self.tweetList.append( message.value)
        return self.tweetList
        
        

class MintParse:
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
    
    def parseString(self, string):
        try:
            tweet = json.loads(string)
            self.parseUrl(tweet)
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
             #print "appending ", url["expanded_url"]
             self.urlList.append(url["expanded_url"])
        
    def extractUrlsFromTweets(self):
        for tweet in self.data:
            self.parseUrl(tweet )
                    
                    
    def printUrls(self):
        for url in self.urlList:
            print url
        

    def getUrlList(self):
        return self.urlList
#
#print "inicio"
##mp = MintParse()
##mp.printUrls()
#
#mc = MintConsumer()
#mc.consume()
#
#print "fin"

