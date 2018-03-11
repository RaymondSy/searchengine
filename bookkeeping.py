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
    db = client.invertedindex2
    posts = db.index
    while True:
        try:
            bookkeeping = bookparser()
            search = raw_input("Search: ").split(' ')
            if len(search) > 1:
                result1 = posts.find_one({'token': search[0]})['records']
                result2 = posts.find_one({'token': search[1]})['records']
                docID2 = []
                urls = []
                for document in result2:
                    docID2.append(document['docID'])
                for document in result1:
                    if document['docID'] in docID2:
                        urls.append(document)
                for document in sorted(urls[:10], key = lambda k: k['tfidf'], reverse=True):
                    if not (len(bookkeeping[document['docID']]) > 500):
                        print ("URL: " + bookkeeping[document['docID']])
                        print ("TFIDF: " + str(document['tfidf']))



            else:
                result = posts.find_one({'token': search[0]})
                for document in sorted(result['records'][:10], key = lambda k: k['tfidf'], reverse=True):
                    if not (len(bookkeeping[document['docID']]) > 200):
                        print ("URL: " + bookkeeping[document['docID']])
                        print ("TFIDF: " + str(document['tfidf']))
                    # print document

        except:
            print "File not found"


if __name__ == "__main__":
    main()