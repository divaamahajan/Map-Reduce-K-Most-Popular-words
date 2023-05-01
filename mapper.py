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


def read_chunk(file_path, chunk_start, chunk_size):
    with open(file_path, "r") as file:
        file.seek(chunk_start)
        chunk = file.read(chunk_size)
    return chunk


def process_chunk(chunk, stop_words):
    word_counts = defaultdict(int)
    for line in chunk.splitlines():
        for word in re.findall(r"\w+", line.lower()):
            if word and word not in stop_words:
                word_counts[word] += 1
    return word_counts


def main():
    # read stop words from file
    stop_words = read_stop_words("stop_words.txt")

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    # read the input data
    input_file = args.input_file
    file_size = os.path.getsize(input_file)
    chunk_size = 64 * 1024 * 1024 # 64 MB

    # create a list of chunks
    chunks = []
    offset = 0
    while offset < file_size:
        chunk_end = min(offset + chunk_size, file_size)
        chunks.append((offset, chunk_end))
        offset = chunk_end

    # process each chunk and output the intermediate key-value pairs
    for chunk_start, chunk_end in chunks:
        chunk = read_chunk(input_file, chunk_start, chunk_size)
        word_counts = process_chunk(chunk, stop_words)
        for word, count in word_counts.items():
            print(f"{word}\t{count}")


if __name__ == '__main__':
    main()
