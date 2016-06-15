# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 07:35:10 2016

@author: jortilles
"""


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import PIL
from PIL import Image

class MintScrapSnapShoot:

    #data['key'] = 'value'

    def __init__(self, url , image):
        print "generating image"
        browser = webdriver.PhantomJS()
        browser.set_page_load_timeout(20)
        browser.set_window_size(1024, 768) 
        try:
            browser.get(url)
            browser.save_screenshot(image)
            browser.quit()
            self.resize(image)
        except TimeoutException as e:
            #Handle your exception here
            #print(e)
            print "session expired  Image "  , image, " not generated "
        finally:
            browser.quit()        
            
        print "image " , image, " done"
        
        
    def resize(self, image):
        print "Resizing image"
        basewidth = 300
        img = Image.open( image )
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
        img.crop((0, 0, basewidth, 250))
        img.save("tm_" + image)