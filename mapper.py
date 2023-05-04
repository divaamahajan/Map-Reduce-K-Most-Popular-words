import re
import os
from collections import defaultdict
import argparse

# Define function to read stop words from a file
def read_stop_words(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as sw:
        stop_words = set()
        for line in sw:
            # Add words in each line of the file as a set to the stop_words set
            stop_words.update(line.strip().split(","))
        # Return the set of stop words
        return stop_words


def mapper():
    # read stop words from file
    stop_words = read_stop_words("stop_words.txt")
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = re.findall(r"\w+", line.lower())
        # create a dictionary to store the word counts
        word_counts = defaultdict(int)
        # iterate over the words
        for word in words:
            # if the word is not in the stop words set, increment its count in the dictionary
            if word not in stop_words:
                word_counts[word] += 1
        # emit the word counts as key-value pairs
        for word, count in word_counts.items():
            print(f"{word}\t{count}")


if __name__ == '__main__':
    mapper()
