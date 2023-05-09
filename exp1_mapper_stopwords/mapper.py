#!/usr/bin/env python3
import re
from collections import defaultdict
import sys
import os
import logging
import time


# get the absolute path of the directory 
dir_path = os.path.dirname(os.path.dirname(__file__))
# append the relative path of stop_words.txt to the directory path
STOP_WORDS = os.path.join(dir_path, 'stop_words.txt')

# Define function to read stop words from a file
def read_stop_words(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        return set([word.lower() for word in f.read().splitlines()])


def mapper():
    # read stop words from file
    stop_words = read_stop_words(STOP_WORDS)
    # create a dictionary to store the word counts
    word_counts = defaultdict(int) 

    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # convert line to lowercase and split into words
        words = re.findall(r"\w+", line.lower())
        # iterate over the words
        for word in words:
            # if the word is not in the stop words set, increment its count in the dictionary
            if word not in stop_words:
                word_counts[word] += 1
    # emit the word counts as key-value pairs
    for word, count in word_counts.items():
        print(f"{word}\t{count}")

if __name__ == '__main__':
    
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    start_time = time.time()
    mapper()
    end_time = time.time()
    logging.info(f"********************* Mapper Total runtime: {end_time - start_time} seconds")