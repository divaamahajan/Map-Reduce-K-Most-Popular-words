#!/usr/bin/env python3
from collections import defaultdict
import sys
import os
# get the absolute path of the directory 
dir_path = os.path.dirname(os.path.dirname(__file__))
# append the relative path of stop_words.txt to the directory path
STOP_WORDS = os.path.join(dir_path, 'stop_words.txt')

print(STOP_WORDS)
# Define function to read stop words from a file
def read_stop_words(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        return set([word.lower() for word in f.read().splitlines()])
    
def reducer():
    # read stop words from file
    stop_words = read_stop_words(STOP_WORDS)
    # create a dictionary to store the word counts
    word_counts = defaultdict(int)
    
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        
        # parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        #skip stopwords
        if word in stop_words: continue
        
        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            continue
        
        # add the count to the dictionary
        word_counts[word] += count

    # Emit the top k words as key-value pairs
    for count, word in word_counts:
        print(f"{word}\t{count}")


if __name__ == '__main__':
    reducer()
