import json
from pprint import pprint

def bookparser():
    file = "/Users/Raymond/PycharmProjects/searchengine/bookkeeping.json"
    # with open(file) as data_file:
    data = json.load(open(file))

def main():

    try:
        bookparser()
    except:
        print "File not found"


if __name__ == "__main__":
    main()