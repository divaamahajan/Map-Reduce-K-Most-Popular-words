#!/bin/bash

start_time=$(date +%s.%N)

# Run the MapReduce job
hadoop-3.3.5/bin/hadoop jar hadoop-3.3.5/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-file exp1_stopwords/mapper.py \
-mapper "python3 mapper.py" \
-file exp1_stopwords/reducer_stopwords.py \
-reducer "python3 reducer_stopwords.py" \
-input /user/divyamahajan/MapReduce/input/data_16GB.txt \
-output /user/divyamahajan/MapReduce/output/topk_redstop.txt

# Capture the performance metrics
end_time=$(date +%s.%N)
runtime=$(echo "$end_time - $start_time" | bc)
cpu_time=$(grep "Mapper" /tmp/hadoop-*/*/syslog | awk '{print $8}' | sed 's/[^0-9.]*//g' | awk '{s+=$1} END {print s}')
memory_usage=$(grep "Maximum resident" /tmp/hadoop-*/*/syslog | awk '{print $6}' | sed 's/[^0-9]*//g' | awk '{s+=$1} END {print s}')

# Write the metrics to a CSV file in the output directory
echo "mapper,reducer,Runtime,CPU time,Memory usage" > /tmp/performance.csv
echo "mapper.py,reducer_stopwords.py,$runtime,$cpu_time,$memory_usage" >> /tmp/performance.csv
hadoop-3.3.5/bin/hadoop fs -put /tmp/performance.csv /user/divyamahajan/MapReduce/output/

# Print the metrics to the console
echo "Runtime,CPU time,Memory usage"
echo "$runtime,$cpu_time,$memory_usage"
