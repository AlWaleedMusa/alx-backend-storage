#!/usr/bin/env python3
'''Task 9'.
'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document.
    '''

    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
