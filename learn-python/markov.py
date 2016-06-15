# You must have pymarkovchain in your path
# https://github.com/TehMillhouse/PyMarkovChain
import sys
from pymarkovchain import MarkovChain
import glob
import os


# wordpoolGen will generate a list of words from all available .txt.files in the working directory
def wordpool_generator():
    wordpool = []

    # The following iterator will run through all .txt file in the directory
    # print the name and replace newlines with spaces
    for file in glob.glob("*.txt"):
        print(file)
        wordpool.append(open(file).read().replace('\n', ' '))

    # Next, the function will put all texts in one string and remove numbers
    wordpool = ' '.join(wordpool)
    wordpool = ''.join([i for i in wordpool if not i.isdigit()])
    return wordpool


# databaseGen will generate and dumb a database.
def database_generator(markovChain, wordpool):
    markovChain.generateDatabase(wordpool)
    markovChain.dumpdb()


# stringGen will generate a string, based on the markov database.
def string_generator(markovChain):
    while True:
        markovString = markovChain.generateString()

        # The function will keep generating new strings
        # until it makes a string longer than 50 characters and shorter than 140 (Twitter limit)
        if len(markovString) > 50 and len(markovString) < 140:
            return markovString


# The main script will
# 1. connect to a Markov database
# 2. generate a word pool and a database if it doesn't exist already
# 3. generate a string from the markovChain and output it
if __name__ == '__main__':
    databaseName = '.\database.p'
    markovChain = MarkovChain(databaseName)
    if not os.path.isfile(databaseName):
        wordpool = wordpool_generator();
        database_generator(markovChain, wordpool)
    else:
        print('Database already exists, skipping database creation...')
    string = string_generator(markovChain)
    print(sys.stdout.encoding)
    print(string.encode('latin1').decode('utf8'))