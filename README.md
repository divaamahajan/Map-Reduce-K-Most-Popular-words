# Map-Reduce-K-Most-Popular-words
## COEN 242 Big Data - Programming Assignment 2
### Student name(s) - Divya Mahajan, Rushang Shah

---

## Steps to run the MapReduce program

Prerequisite - Hadoop should be installed and configured in your system. The word count program’s data set should already be copied in the HDFS. We are using Python programming, so please edit the `.py` file first line with the Python compiler location (mostly `/usr/bin/python` or `/usr/bin/python3`).

1. Download the source code from GitHub - [GitHub Repository](https://github.com/divaamahajan/Map-Reduce-K-Most-Popular-words.git).
2. Save the git repository at a desired location.
3. Open the terminal/command prompt and navigate to the directory where you want to save the output files.
4. Copy the following command exactly, replacing the variables as explained below:
	
	```shell
	hadoop jar *a* -input *b* -mapper *c* -reducer *d* -numReduceTasks *e* -output *f* > *g* 2>&1 
	```
	
	- `*a*`: Location of Hadoop streaming jar file, usually found at `$HADOOP_HOME/share/hadoop/tools/lib/`.
	- `*b*`: Location of the input data set in the HDFS file system.
	- `*c*`: Location of the mapper file depending upon your desired experiment. It can be either in HDFS or local system. Since we are using a Python program, please use `python3 <location of file>` in the mapper.
	- `*d*`: Location of the reducer file depending upon your desired experiment. It can be either in HDFS or local system. Since we are using a Python program, please use `python3 <location of file>` in the reducer.
	- `*e*`: If you want to use a specific number of reducers, you can use this option. Before using it, make sure you have properly configured `core-site.xml`, `hdfs-site.xml`, and `yarn-site.xml`. Alternatively, you can pass such a configuration option in a file with `-conf` in the above command.
	- `*f*`: Location to store the output result of the reducer in HDFS.
	- `*g*`: Log file name for console logs to be saved, generated by Hadoop.

	Example of the above command (you can modify the file paths in the below example):

	```shell
	hadoop jar /Users/<username>/hadoop-3.2.3/share/hadoop/tools/lib/hadoop-streaming-3.2.3.jar \
	-input /user/<username>/data_16Gb.txt \
	-mapper "python3 /Users/<username>/SCU/BigData/HW2/Git/Map-Reduce-K-Most-Popular-words/exp4_6plusTopk/mapper.py" \
	-reducer "python3 /Users/<username>/SCU/BigData/HW2/Git/Map-Reduce-K-Most-Popular-words/exp4_6plusTopk/reducer.py" \
	-numReduceTasks 1 \
	-output /user/<username>/output > consoleLog.txt 2>&1
	```
	
5. After running this command, three files will be generated in the directory:
	- Log file containing the console logs generated by Hadoop.
	- `mapper.csv` file, which contains process ID, runtime, memory usage, CPU utilization for each mapper
	- `reducer.csv` file, which contains process ID, runtime, memory usage, CPU utilization for each mapper

6. Download the output generated by reducer
	-` hadoop fs -getmerge /user/<username>/output  ~/Users/Public/Map-Reduce-K-Most-Popular-words/outputs/reducerOutput.txt`

7. Apply topK algorithm
 - `cat .\outputs\reducerOutput.txt | python topK\topk.py > outputs\top100Output.txt `

## Note: Reducing the number of mappers and changing the block size

If you want to reduce the number of mappers while saving the file in HDFS, you can change the default block size of 128MB. Use the following command:

```shell
hadoop fs -Ddfs.blocksize=<block size in bytes> -put <local file path to the file> <HDFS path to save file>
```

Replace the following parameters:

- `<block size in bytes>`: Specify the desired block size in bytes.
- `<local file path to the file>`: Provide the local file path of the file you want to save in HDFS.
- `<HDFS path to save file>`: Specify the HDFS path where you want to save the file.

For example:

```shell
hadoop fs -Ddfs.blocksize=67108864 -put /path/to/local/file.txt /user/username/data/file.txt
```

This command will put the file `file.txt` from the local file system at the specified block size into the `/user/username/data/` directory in HDFS.
