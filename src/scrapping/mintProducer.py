# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:06:27 2016

@author: jortilles
"""

from pykafka import KafkaClient
import unicodedata

class MintProducer:
    def __init__(self  ):
        self.client = KafkaClient(hosts="127.0.0.1:9092,127.0.0.1:9093")
        self.topic = self.client.topics['crawled_urls']

#with topic.get_sync_producer() as producer:
#    for i in range(4):
#        producer.produce('test message ' + str(i ** 2))
        
    
    def append(self, url):      
        mi_url = unicodedata.normalize('NFKD', url).encode('ascii','ignore')          
        with self.topic.get_sync_producer() as producer:
              producer.produce(mi_url)
              print url, " appended to crawled_urls"
              
 



#mp = MintProducer()
#mp.append("http://www.univision.com/especiales/premios-juventud/de-cabello-negro-o-rubias-como-prefieres-a-estas-bellas-fotos  stored ")