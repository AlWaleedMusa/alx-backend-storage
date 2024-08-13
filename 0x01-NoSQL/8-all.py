#!/usr/bin/env python3
'''Task 8.
'''


def list_all(mongo_collection):
    '''Lists all documents.
    '''
    return [item for item in mongo_collection.find()]
