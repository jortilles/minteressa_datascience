pi# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:35:20 2016

@author: jortilles
"""

from minteressaScrap import  MintScrap
from minteressaScrapSnapShoot import MintScrapSnapShoot
from mintConsumer import MintConsumer
from mintProducer import MintProducer
from mintParseTweet import MintParseTweet
import json


#urls = [ "http://www.jortilles.com", "http://taxitronic.com" ]

tweetsUrls = []
mc = MintConsumer()
tweets = mc.getTweetsFromKafka()




for tweet  in tweets:
    mp = MintParseTweet()
    urls = mp.parseString(tweet)
    my_tweet = json.loads(tweet)
    my_tweet['Minteressa']= []
    for url  in urls:
        print  'Scrapping : ' , url
        print "---------"
        #try:
        ms = MintScrap(url)
        print "url prcessed"
        print "regenerating tweet"
       
        print "appendig info to tweet"
        
        my_tweet['Minteressa'].append( ms.get() )
    
    
    with open('data.txt', 'w') as outfile:
        json.dump(my_tweet, outfile)
    print json.dumps(my_tweet, sort_keys=True,indent=4, separators=(',', ': ')) 
    mp = MintProducer()
    mp.returnTweet( my_tweet )
print 'done'

        
##        if ms.getUUID():
##            #image =   str(   ms.getUUID()  ) + ".png"
##            #photo = MintScrapSnapShoot( url, image) 
##            #mp.append(url)
##            tweetsUrls.append( ms.get() )
##        else:
##            print "no uuid.... no photo"
#            
#        
#        print "appendig info to tweet"
#        print "tweets urls " , tweetsUrls
#        for elment in tweetsUrls:
#            my_tweet['Minteressa'].append(  elment ) 
#        print "updating the tweet"
#       
#        mp.returnTweet( my_tweet )
#        print my_tweet
#        #except:
#        #    print "error processing ", url 








#ms = MintScrap("http://www.jortilles.com")
#ms.forceScrap("http://www.jortilles.com")