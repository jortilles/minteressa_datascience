# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:35:20 2016

@author: jortilles
"""

from minteressaScrap import  MintScrap
from minteressaScrapSnapShoot import MintScrapSnapShoot
from mintConsumer import MintConsumer
from mintProducer import MintProducer

#urls = [ "http://www.jortilles.com", "http://taxitronic.com" ]


mc = MintConsumer()
urls = mc.consume()

#print urls


for url  in urls:
    print  'Scrapping : ' , url
    print "---------"
    ms = MintScrap(url)
    if ms.getUUID():
        image =   str(   ms.getUUID()  ) + ".png"
        photo = MintScrapSnapShoot( url, image) 
        mp = MintProducer()
        mp.append(url)
    else:
        print "no uuid.... no photo"
print 'done'

