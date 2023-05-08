#!/usr/bin/env python3
import sys
from collections import defaultdict

def reducer():
    # create a dictionary to store the word counts
    word_counts = defaultdict(int)
    
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        
        # parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        
        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            continue
        
        # add the count to the dictionary
        word_counts[word] += count
    
    # emit the word counts as key-value pairs
    for word, count in word_counts.items():
        print(f"{word}\t{count}")

if __name__ == '__main__':
    reducer()
