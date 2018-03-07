# Raymond Sy 92546228
import sys
import re
from bs4 import BeautifulSoup
from recordtype import recordtype
from collections import defaultdict

word_dict = defaultdict(list)
Record = recordtype('Record', 'folder page TFIDF')

def readfile(folder, page):
    file = "/Users/Raymond/PycharmProjects/searchengine/WEBPAGES_CLEAN/{}/{}".format(folder, page)
    with open(file, 'r') as f:  # opens the file with read properties
        contents = f.read()  # reads the entire file into a String; python can store up to 2-3gb of data into a string.
    return contents


def tokenize(contents, f, p):
    global word_dict
    soup = BeautifulSoup(contents, 'html.parser')
    #print (soup.get_text())

    tokens = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\w]+", soup.get_text())
    # Finds all the words matching the regex and puts it in a list

    for token in tokens:
        if token.lower() in word_dict:
            documentList = word_dict.get(token.lower())
            #print documentList
            if documentList:
                if not any(doc.folder == f and doc.page == p for doc in documentList):
                    new_record = Record(f, p, 1)
                    word_dict[token.lower()].append(new_record)
                else:
                    for doc in documentList:
                        if doc.folder == f and doc.page == p:
                            doc.TFIDF += 1

        else:
            new_record = Record(f, p, 1)
            word_dict[token.lower()].append(new_record)   # if it doesnt exist, add to dictionary with frequency of 1

    #print word_dict
    # for word, freq in sorted(word_dict.iteritems(), key=lambda(k, v): (-v, k)):
    #     # sort the dictionary by key and by value being reversed
    #     #print word, "-", freq


def main():
    counter = 0
    try:
        # tries to open the file, if any error comes out, jump to except statement
        for i in range(0, 75):
            for x in range(0, 500):
                c = readfile(i,x)
                tokenize(c, i, x)
                counter += 1
                print (counter)
    except:
        print "File not found"

    keys = word_dict.keys()
    values = word_dict.values()
    # for record in zip(keys, values):
    #     print (record[0], ": ", record[1])
    for record in zip(keys,values):
        with open("index3.txt", "a") as fl:
            fl.write(record[0] + ": " + str(record[1]) + "\n")

if __name__ == "__main__":
    main()

