import heapq
import sys


import sys
from collections import defaultdict

def reducer():
    # input comes from STDIN (standard input)
    word_counts = defaultdict(int)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into word and count
        word, count = line.split("\t")
        # convert count (currently a string) to int
        count = int(count)
        # add the count to the running total for the word
        word_counts[word] += count
    # emit the final word counts as key-value pairs

if __name__ == '__main__':
    reducer()
