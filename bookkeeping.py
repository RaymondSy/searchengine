import json
from pprint import pprint
import pymongo
from pymongo import MongoClient


def bookparser():
    file = "/Users/Raymond/PycharmProjects/searchengine/bookkeeping.json"
    # with open(file) as data_file:
    data = json.load(open(file))
    return data

def main():
    client = MongoClient('localhost', 27017)
    db = client.invertedindex
    posts = db.index

    try:
        bookkeeping = bookparser()
        search = raw_input("Search: ")
        result = posts.find_one({'token': search})
        for document in result['records']:
            print bookkeeping[document['docID']]
            print document

    except:
        print "File not found"


if __name__ == "__main__":
    main()