# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:35:20 2016

@author: jortilles
"""

from minteressaScrap import  MintScrap
<<<<<<< HEAD
from minteressaScrapSnapShoot import MintScrapSnapShoot


urls = [ "http://www.jortilles.com", "http://taxitronic.com" ]
=======
from selenium import webdriver

urls = [ "http://www.jortilles.com", "http://taxitronic.com" ]
br = webdriver.PhantomJS()
br.set_window_size(1024, 768)    
>>>>>>> master


for url  in urls:
    print  'Scrapping : ' , url
    ms = MintScrap(url)
    image =   str(   ms.getUUID()  ) + ".png"
<<<<<<< HEAD
    photo = MintScrapSnapShoot( url, image) 

=======
    br.get(url)
    br.save_screenshot(image)


br.quit()
    
>>>>>>> master
        
print 'done'


<<<<<<< HEAD




=======
>>>>>>> master
