import json
from pprint import pprint
import pymongo
import math
from pymongo import MongoClient


def tdidfCalc():
    client = MongoClient('localhost', 27017)
    db = client.invertedindex
    posts = db.index
    documents = posts.find({})
    #documents = posts.find_one({'token': 'cool'})
    for doc in documents:
        postings = len(doc['records'])
        l = [(index, record) for index, record in enumerate(doc['records'])]
        for index, record in l:
            # print record
            tf = math.log10(record['Frequency'])
            idf = math.log10((37497/postings))
            tfidf = tf*idf
            record['tfidf'] = tfidf
            posts.update(
                {'_id': doc['_id']},
                {'$set': {"records.{}.tfidf".format(index): tfidf}},
                upsert=False
            )
            print(record)
            # posts.update_one({'docID': record['docID']}, {"$set": record}, upsert=False)
            # d = posts.find_one({'token': 'cool'})
            # print(d)
            # print("frequency: ", record['Frequency'])
            # print("tf: ", tf)
            # print("idf: ", idf)
            # print("tfidf: ", tfidf)



def main():
    tdidfCalc()
    # client = MongoClient('localhost', 27017)
    # db = client.invertedindex
    # posts = db.index
    # bills_post = posts.find({})
    # for item in bills_post:
    #     print(item['tfidf'])



# result = posts.find_one({'token': search})
# for document in result['records']:
#     print bookkeeping[document['docID']]

if __name__ == "__main__":
    main()

