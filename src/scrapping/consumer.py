# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:06:27 2016

@author: jortilles
"""

from pykafka import KafkaClient


class MintConsumer:

    def __init__(self  ):
        self.client = KafkaClient(hosts="127.0.0.1:9092,127.0.0.1:9093")
        self.topic = self.client.topics['TutorialTopic']

#with topic.get_sync_producer() as producer:
#    for i in range(4):
#        producer.produce('test message ' + str(i ** 2))
        
    
    def consume(self):        
        self.consumer = self.topic.get_simple_consumer()
        for message in self.consumer:
            print message.offset, message.value
    
    
