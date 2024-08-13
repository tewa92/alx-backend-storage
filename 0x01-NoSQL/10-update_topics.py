#!/usr/bin/env python3
''' updates school document '''

def update_topics(mongo_collection, name, topics):
    ''' updates all topics of a school document '''
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})