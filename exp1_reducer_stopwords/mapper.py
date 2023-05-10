#!/usr/bin/env python3
import re
from collections import defaultdict
import sys
import psutil
import logging
import time
import os

def mapper():
    # Get the file descriptor of sys.stdin
    fd = sys.stdin.fileno()

    # Get the size of the file descriptor
    size = os.fstat(fd).st_size
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
    
    return size

def generateLogs(fileSize, start_time, end_time):
    running_time = end_time - start_time
    PID = os.getpid()
    process = psutil.Process(PID)
    memory_usage = process.memory_info().rss
    cpu_utilization = psutil.cpu_percent(interval=running_time)
    logging.info(f"{PID}, {fileSize /1024 /1024: .4f}, {running_time:.2f}, {memory_usage / 1024 / 1024:.2f}, {cpu_utilization:.2f}")

if __name__ == '__main__':
    logging.basicConfig(filename='mapper.csv', format='%(asctime)s %(message)s',level=logging.INFO)
    start_time = time.time()
    fileSize = mapper()
    end_time = time.time()
    generateLogs(fileSize,start_time,end_time)
