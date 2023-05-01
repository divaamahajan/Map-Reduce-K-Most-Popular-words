import heapq
import sys

def main():
    # set the number of top words to find
    # k = int(input("Enter the number of top words to find: "))
    k = 10

    # read the intermediate key-value pairs from stdin
    word_counts = {}
    for line in sys.stdin:
        word, count = line.strip().split('\t')
        word_counts[word] = word_counts.get(word, 0) + int(count)

    # get the top k frequent words
    top_k_words = heapq.nlargest(k, word_counts.items(), key=lambda x: x[1])

    # output the top k frequent words to stdout
    print("\nTop frequent words:")
    print("Word".ljust(21) + "Count")
    print("--------------------------")
    for word, count in top_k_words:
        print("{:<20} {}".format(word, count))

if __name__ == '__main__':
    main()
