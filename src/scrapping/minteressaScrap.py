# -*- coding: utf-8 -*-
"""
Editor de Spyder



Scrapper fo m'interessa
"""
import whois
import requests
import json
import re
from urlparse import urlparse
from bs4 import BeautifulSoup
import uuid
from pymongo import MongoClient
#from urllib import urlopen

from os import path

class MintScrap:

    #data['key'] = 'value'

    def __init__(self, url ):
        self.url = url
        
        self.data = {  "metadata":{\
                       "whois":{"whoisName":"name", "whoisOrg":"org", "whoisCity":"city", "whoisCountry":"ES"} ,   \
                       "urlparse":{"scheme":"scheme", "hostname":"hostname", "netloc":"netloc", "port":"port", "path":"path", "params":"params", "query":"query", "fragment":"fragment", "username":"username", "password":"password" } , \
                       "header":{"title":"title", "contentLanguage":"contentLanguage", "contentType":"contentType", "description":"description", "author":"author", "copyright":"copyright", "generator":"generator", "subject":"subject", "abstract":"abstract", "topic":"topic" , "keywords":["keywords"]  },  \
                       "url": self.url  , \
                       "UUID": uuid.uuid4()  , \
                       "schemaPresent": "no" \
                        },  \
                    "content":{ \
                        "text": {"text":"text", "length":55 }, \
                        "links": { "total":[], "internal":[],"external":[], "social":{"twitter":[], "facebook":[], "reddit":[], "meneame":[] }} , \
                        "imgs":[{ "file":"file", "alt":"alt", "title":"title", "width":"widht", "height":"height"}] \
                    } \
                }
        
        self.paraseUrl()
        self.whois()
        self.soup()
        #self.info() 
        self.store()
        
    def getUUID(self):
        return self.data["metadata"]["UUID"]
        
    def info(self):
        print "===================MintScrap Info==================="
        print "Processing ", self.url
        print json.dumps(self.data, sort_keys=True,indent=4, separators=(',', ': ')) 
        print "===================MintScrap Info==================="
        
    def whois(self ):
        res = whois.whois(  self.data["metadata"]["urlparse"]["hostname"]   )
        self.data["metadata"]["whois"]["whoisName"]  = res.name
        self.data["metadata"]["whois"]["whoisOrg"]  = res.org
        self.data["metadata"]["whois"]["whoisCity"]  = res.city
        self.data["metadata"]["whois"]["whoisCountry"]  = res.country

    def paraseUrl(self):
        o = urlparse( self.url )
        self.data["metadata"]["urlparse"]["scheme"]  = o.scheme
        self.data["metadata"]["urlparse"]["netloc"]  = o.netloc
        self.data["metadata"]["urlparse"]["hostname"]  = o.hostname
        self.data["metadata"]["urlparse"]["port"]  = o.port
        self.data["metadata"]["urlparse"]["path"]  = o.path
        self.data["metadata"]["urlparse"]["params"]  = o.params
        self.data["metadata"]["urlparse"]["query"]  = o.query
        self.data["metadata"]["urlparse"]["fragment"]  = o.fragment
        self.data["metadata"]["urlparse"]["username"]  = o.username
        self.data["metadata"]["urlparse"]["password"]  = o.password


    def soup(self):
        r = requests.get( self.url )
        html = r.text
        #self.data["content"]["stream"] = html
        soup = BeautifulSoup(html, 'html5lib')  
        self.headersUrl( soup, r)
        # self.getlinks( html) not used because we user the getSoupLinks to get more info
        self.getSoupLinks( soup)
        self.getImages(soup)
        self.checkSchema(html)
        # get text
        text = soup.get_text()       
        self.getText(text)       
        


    def  checkSchema(self, html):   
        if "itemscope" in html:
            self.data["metadata"]["schemaPresent"] = True
        else:
            self.data["metadata"]["schemaPresent"] = False

            
        
    def getText(self, text):  
        
        cleantext = text.replace('\n', ' ').replace('\r', '')
        cleantext = cleantext.replace( '\t',' ')
        
        cleantext = re.sub(' +',' ',cleantext)
        # css class
        cleantext = re.sub('\.[^\.]+\}',' ',cleantext) 
        cleantext = re.sub('<+.?>', '', cleantext)
        cleantext = re.sub('<!--+.?-->', '', cleantext)
        cleantext = re.sub('\/\*.?\*\/', '', cleantext)
        #print 'POST ::::::::::::::' , cleantext  
               
        #print 'pre ::::::::::::::' , cleantext        
        cleantext = re.sub('funct.+}',' ',cleantext)
        #cleantext = re.sub('\{[^\{]+\}',' ',cleantext)
        #print ""
        #print 'POST ::::::::::::::' , cleantext           
        self.data["content"]["text"]["text"]   = cleantext
        words =     cleantext.split(' ')    
        self.data["content"]["text"]["length"]   =  len(words)

        


    def getImages(self, soup): 
        imgs = []
        for image in soup.findAll("img"): 
            img = { }
            #img["img"] = image
            img["file"] = image.get('src','')
            img["alt"] = image.get('alt','')    
            img["title"] = image.get('title','')
            img["width"] = image.get('width','')
            img["height"] = image.get('height','')
            imgs.append(img)
        self.data["content"]["imgs"]   = imgs




    def getSoupLinks(self, soup ): 
        links = []
        for link in soup.findAll('a', href=True):
            # skip useless links
            if link['href'] == '' or link['href'].startswith('#'):
                continue
            # initialize the link
            thisLink = {}
            thisLink["url"] =  link['href']
            thisLink["title"] =    link.string,
            thisLink["image"] =     "image" 
        
            # see if the link contains an image
            img = link.find('img', src=True)
            if img:
                thisLink["image"] = img['src']
                if thisLink["title"] is None:
                    # look for a title here if none exists
                    if "title" in img:
                        thisLink["title"] = img["title"]
                    elif "alt" in img:
                        thisLink["title"] = img["alt"]
                    else:
                        thisLink["title"] = path.basename(img["src"])
        
            if thisLink["title"] is None:
                # check for text inside the link
                if len(link.contents):
                    thisLink["title"] = link.stripped_strings
            if thisLink["title"] is None:
                # if there's *still* no title (empty tag), skip it
                continue
            # store the result
            if thisLink not in links:
                links.append(thisLink)
        
        # appeind to the total
        self.data["content"]["links"]["total"] = links
         
         
        # appeind to the internal / external 
        external_regexp = re.compile('^http|^ftp', re.IGNORECASE)
        internalLinks = []
        extenalLinks = []
        for lk in links: 
            if  external_regexp.search(lk["url"]) :
                extenalLinks.append(lk)
                #print "link EXTERNO " , link
            else:
                internalLinks.append(lk)
                #print "link  interno ", link
        self.data["content"]["links"]["internal"]  = internalLinks
        self.data["content"]["links"]["external"]  = extenalLinks              
                
        facebook = []
        twitter = []
        reddit = []
        meneame = []
        for link in links:
            if 'facebook' in link["url"]:
                facebook.append(link)
            if 'facebook' in link["url"]:
                facebook.append(link)
            elif 'twitter' in link["url"]:
                twitter.append(link)
            elif 'reddit' in link["url"]:
                reddit.append(link)
            elif 'meneame' in link["url"]:
                meneame.append(link)
    
        self.data["content"]["links"]["social"]["facebook"]  =   facebook 
        self.data["content"]["links"]["social"]["twitter"]  =   twitter 
        self.data["content"]["links"]["social"]["reddit"]  =   reddit 
        self.data["content"]["links"]["social"]["meneame"]  =   meneame        
            


    def getlinks(self, html ): 
        webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
        external_regexp = re.compile('^http|^ftp', re.IGNORECASE)
        
        linksArr = webpage_regex.findall(html)
        self.data["content"]["links"]["total"]  = linksArr

        internalLinks = []
        extenalLinks = []
        for link in linksArr: 
            if  external_regexp.search(link) :
                extenalLinks.append(link)
                #print "link EXTERNO " , link
            else:
                internalLinks.append(link)
                #print "link  interno ", link

        self.data["content"]["links"]["internal"]  = internalLinks
        self.data["content"]["links"]["external"]  = extenalLinks
        
        facebook = []
        twitter = []
        reddit = []
        meneame = []
        for link in extenalLinks:
            if 'facebook' in link:
                facebook.append(link)
            elif 'twitter' in link:
                twitter.append(link)
            elif 'reddit' in link:
                reddit.append(link)
            elif 'meneame' in link:
                meneame.append(link)
    
        self.data["content"]["links"]["social"]["facebook"]  =   facebook 
        self.data["content"]["links"]["social"]["twitter"]  =   twitter 
        self.data["content"]["links"]["social"]["reddit"]  =   reddit 
        self.data["content"]["links"]["social"]["meneame"]  =   meneame 

    
        
    def headersUrl( self, soup, r):
        try:
            title = soup.title.string
        except:
            title = 'NaN'
        self.data["metadata"]["header"]["title"]  = title
        try:
            contentLanguage= r.headers['Content-language']
        except:
            contentLanguage = 'NaN'
        self.data["metadata"]["header"]["contentLanguage"]  = contentLanguage
        try:
            contentType = r.headers['Content-type']
        except:
            contentType = 'NaN'
        self.data["metadata"]["header"]["contentType"]  = contentType
        # Not really ellegant but funtional.... 
        description= soup.find(attrs={'name':'Description'})
        if description == None:
            description= soup.find(attrs={'name':'description'})
        try:
            description = description['content']
        except:
            description = 'NaN'
        self.data["metadata"]["header"]["description"]  = description
        # Not really ellegant but funtional.... 
        author= soup.find(attrs={'name':'Author'})
        if author == None:
            author= soup.find(attrs={'name':'author'})
        try:
            author = author['content']
        except:
            author = 'NaN'
        self.data["metadata"]["header"]["author"]  = author   
        # Not really ellegant but funtional.... 
        copyright= soup.find(attrs={'name':'Copyright'})
        if copyright == None:
            copyright= soup.find(attrs={'name':'copyright'})
        try:
            copyright = copyright['content']
        except:
            copyright = 'NaN'
        self.data["metadata"]["header"]["copyright"]  = copyright   
        # Not really ellegant but funtional.... 
        keywords= soup.find(attrs={'name':'Keywords'})
        if keywords == None:
            keywords= soup.find(attrs={'name':'keywords'})
        try:
            keywords = keywords['content']
        except:
            keywords = 'NaN'
        self.data["metadata"]["header"]["keywords"]  = keywords.split(',')   
        # Not really ellegant but funtional.... 
        generator= soup.find(attrs={'name':'Generator'})
        if generator == None:
            generator= soup.find(attrs={'name':'generator'})
        try:
            generator = generator['content']
        except:
            generator = 'NaN'
        self.data["metadata"]["header"]["generator"]  = generator             
        # Not really ellegant but funtional.... 
        subject= soup.find(attrs={'name':'Subject'})
        if subject == None:
            subject= soup.find(attrs={'name':'subject'})
        try:
            subject = subject['content']
        except:
            subject = 'NaN'
        self.data["metadata"]["header"]["subject"]  = subject  
        # Not really ellegant but funtional.... 
        abstract= soup.find(attrs={'name':'Abstract'})
        if abstract == None:
            abstract= soup.find(attrs={'name':'abstract'})
        try:
            abstract = abstract['content']
        except:
            abstract = 'NaN'
        self.data["metadata"]["header"]["abstract"]  = abstract     
        # Not really ellegant but funtional.... 
        topic= soup.find(attrs={'name':'Topic'})
        if topic == None:
            topic= soup.find(attrs={'name':'topic'})
        try:
            topic = topic['content']
        except:
            topic = 'NaN'
        self.data["metadata"]["header"]["topic"]  = topic   
        

    def store(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.urls
        collection = db.urls
        if collection.find_one( {"metadata.url": self.data["metadata"]["url"] }  ) :
            print self.data["metadata"]["url"] , " already exists "
        else : 
            collection.insert(self.data)
            print self.data["metadata"]["url"] , " stored "
        




