import json

def bookparser():
    file = "/Users/Raymond/PycharmProjects/searchengine/bookkeeping.json"
    with open(file) as data_file:
        data = data_file.read()
        j = json.loads(data)
        print j['9/86']

def indexloader():
    file = "/Users/Raymond/PycharmProjects/searchengine/index3.txt"
    with open(file) as data_file:
        data = data_file.read()
        content = data.split(":")
    print content

def main():

    try:
        bookparser()
        indexloader()
    except:
        print "File not found"


if __name__ == "__main__":
    main()