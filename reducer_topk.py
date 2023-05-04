
import sys
import heapq

def reducer_topk():
    k = 10
    # input comes from STDIN (standard input)
    topk_heap = []
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into word and count
        word, count = line.split("\t")
        # convert count (currently a string) to int
        count = int(count)
        # add the count to the heap
        heapq.heappush(topk_heap, (-count, word))
    # emit the final top-k word counts as key-value pairs
    for i in range(k):
        count, word = heapq.heappop(topk_heap)
        count = -count
        print(f"{word}\t{count}")


if __name__ == '__main__':
    reducer_topk()
