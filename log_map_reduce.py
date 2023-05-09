import logging

# Configure logging to write to a file
logging.basicConfig(filename='map_reduce.log', level=logging.INFO)

def mapper():
    # Your mapper code here
    pass

def reducer():
    # Your reducer code here
    pass

if __name__ == '__main__':
    # Log the number of InputSplits
    logging.info('Number of InputSplits: %s', 10)

    # Run the mapper and log the number of partitions
    mapper()
    logging.info('Number of Partitions: %s', 5)

    # Log the number of reducer and mapper tasks
    logging.info('Number of reducer tasks: %s', 3)
    logging.info('Number of mapper tasks: %s', 10)

    # Log the size of each partition
    logging.info('Size of each partition: %s', [1024, 2048, 3072, 4096, 5120])

    # Log the memory allocated for each reducer and mapper
    for i in range(3):
        logging.info('Memory allocated for reducer %s: %s', i, 2048)
    for i in range(10):
        logging.info('Memory allocated for mapper %s: %s', i, 512)

    # Log the chunk processed by each reducer and mapper
    for i in range(3):
        logging.info('Chunk processed by reducer %s: %s', i, 1024)
    for i in range(10):
        logging.info('Chunk processed by mapper %s: %s', i, 512)

    # Log the size of the output generated by the mapper tasks
    logging.info('Size of the output generated by the mapper tasks: %s', 4096)

    # Log the mapper and reducer running time
    logging.info('Mapper running time: %s', 100)
    logging.info('Reducer running time: %s', 50)

    # Log the memory usage and CPU utilization
    logging.info('Memory usage: %s', 8192)
    logging.info('CPU utilization: %s', 80)