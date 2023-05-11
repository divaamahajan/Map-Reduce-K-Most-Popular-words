#!/usr/bin/env python3
import sys
import heapq
import logging
import time
import sys
import logging
import time
import os
import psutil


k = 100

def topk():
    # Get the file descriptor of sys.stdin
    fd = sys.stdin.fileno()

    # Get the size of the file descriptor
    size = os.fstat(fd).st_size
    # Use a heap to keep track of the top k words
    top_words = []    
    
    # iterate through each key-value pair from the reducer
    for line in sys.stdin:
        # parse the key-value pair
        word, count = line.split("\t")
        count = int(count)
        if len(word)< 7: continue
        # add word to the top k list if count is greater than smallest count in list
        if len(top_words) < k:
            heapq.heappush(top_words, (count, word))
        else:
            if count > top_words[0][0]:
                heapq.heappushpop(top_words, (count, word))

    # Emit the top k words as key-value pairs
    for count, word in top_words:
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
    # logging.basicConfig(filename='topk.csv',format='%(asctime)s %(message)s',level=logging.INFO)
    # start_time = time.time()
    fileSize = topk()
    # end_time = time.time()
    # generateLogs(fileSize, start_time,end_time)
