#!/usr/bin/env python3
import sys
from collections import defaultdict
import logging
import time
import os
import psutil

def reducer():
    # Get the file descriptor of sys.stdin
    fd = sys.stdin.fileno()

    # Get the size of the file descriptor
    size = os.fstat(fd).st_size
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
    
    return size



def generateLogs(fileSize, start_time, end_time):
    # Generate logs containing process information such as PID, file size, runtime, memory usage, and CPU utilization.
    running_time = end_time - start_time
    PID = os.getpid()
    process = psutil.Process(PID)
    memory_usage = process.memory_info().rss
    cpu_utilization = psutil.cpu_percent(interval=running_time)
    logging.info(f"{PID}, {fileSize /1024 /1024: .4f}, {running_time:.2f}, {memory_usage / 1024 / 1024:.2f}, {cpu_utilization:.2f}")


if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(filename='reducer6.csv', format='%(asctime)s %(message)s', level=logging.INFO)
    # Uncomment the line below if you want to include a header in the log file
    # logging.info('Timestamp, PID, File read size(MB), Runtime(seconds), Memory Usage(MB), CPU utilization (%)')

    # Start the timer
    start_time = time.time()

    # Execute the reducer function and get the file size
    fileSize = reducer()
    
    # Stop the timer
    end_time = time.time()

    # Generate the logs
    generateLogs(fileSize, start_time, end_time)

