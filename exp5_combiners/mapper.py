#!/usr/bin/python3
import re
import sys
import os
import logging
import time
import psutil

# get the absolute path of the directory 
dir_path = os.path.dirname(os.path.dirname(__file__))
# append the relative path of stop_words.txt to the directory path
STOP_WORDS = os.path.join(dir_path, 'stop_words.txt')

# Define function to read stop words from a file
def read_stop_words(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        return set([word.lower() for word in f.read().splitlines()])


def mapper():
    # Get the file descriptor of sys.stdin
    fd = sys.stdin.fileno()

    # Get the size of the file descriptor
    size = os.fstat(fd).st_size

    # read stop words from file
    stop_words = read_stop_words(STOP_WORDS)

    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # convert line to lowercase and split into words
        words = re.findall(r"\w+", line.lower())
        # iterate over the words
        for word in words:
            # if the word is not in the stop words set, increment its count in the dictionary
            if word not in stop_words:
                print(f"{word}\t{1}")
    
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
    logging.basicConfig(filename='mapper5.csv', format='%(asctime)s %(message)s', level=logging.INFO)
    # Uncomment the line below if you want to include a header in the log file
    # logging.info('Timestamp, PID, File read size(MB), Runtime(seconds), Memory Usage(MB), CPU utilization (%)')

    # Start the timer
    start_time = time.time()

    # Execute the mapper function and get the file size
    fileSize = mapper()

    # Stop the timer
    end_time = time.time()

    # Generate the logs
    generateLogs(fileSize, start_time, end_time)

