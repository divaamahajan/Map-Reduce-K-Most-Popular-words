#!/usr/bin/env python3
import re
from collections import defaultdict
import sys

def mapper():
    # create a dictionary to store the word counts
    word_counts = defaultdict(int) 

    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # convert line to lowercase and split into words
        words = re.findall(r"\w+", line.lower())
        # iterate over the words
        for word in words:
            # increment its count in the dictionary
            word_counts[word] += 1
    # emit the word counts as key-value pairs
    for word, count in word_counts.items():
        print(f"{word}\t{count}")

if __name__ == '__main__':
    mapper()
