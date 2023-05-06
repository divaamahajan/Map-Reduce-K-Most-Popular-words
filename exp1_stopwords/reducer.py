import sys
import heapq
k = 100

def reducer():
    # Use a heap to keep track of the top k words
    top_words = []    
    
    # iterate through each key-value pair from the mapper
    for line in sys.stdin:
        # parse the key-value pair
        word, count = line.split("\t")
        count = int(count)

        # add word to the top 10 list if count is greater than smallest count in list
        if len(top_words) < 10:
            heapq.heappush(top_words, (count, word))
        else:
            if count > top_words[0][0]:
                heapq.heappushpop(top_words, (count, word))

    # Emit the top k words as key-value pairs
    for count, word in top_words:
        print(f"{word}\t{count}")

if __name__ == '__main__':
    reducer()
