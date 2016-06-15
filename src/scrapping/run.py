# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:35:20 2016

@author: jortilles
"""

from minteressaScrap import  MintScrap
from minteressaScrapSnapShoot import MintScrapSnapShoot


urls = [ "http://www.jortilles.com", "http://taxitronic.com" ]

for url  in urls:
    print  'Scrapping : ' , url
    ms = MintScrap(url)
    image =   str(   ms.getUUID()  ) + ".png"

    photo = MintScrapSnapShoot( url, image) 

   
print 'done'

