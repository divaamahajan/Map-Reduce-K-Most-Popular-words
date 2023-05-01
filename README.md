# Map-Reduce-K-Most-Popular-words

## To run mapper separately
`python3 mapper.py small_50MB_dataset.txt > intermediate_data.txt`

## To run reducer separately after mapper
`cat intermediate_data.txt | sort | python3 reducer.py`

## To run on local system
`python3 mapper.py small_50MB_dataset.txt | sort | python3 reducer.py > output_50MB.txt`
1. `python3 mapper.py small_50MB_dataset.txt`: This command runs the `mapper.py` script using Python 3 and passes the `small_50MB_dataset.txt` file as an argument. The `mapper.py` script reads the input file and processes it in chunks, generating key-value pairs for each word in the file, where the key is the word and the value is the number of occurrences of the word in the chunk. The output from the `mapper.py` script is a list of key-value pairs printed to the standard output.

2. `sort`: This command sorts the output of the `mapper.py` script in alphabetical order based on the keys. This is necessary because the reducer script expects input data that is sorted by key.

3. `python3 reducer.py`: This command runs the `reducer.py` script using Python 3. The `reducer.py` script reads the sorted key-value pairs from the standard input and performs a "reduce" operation to compute the total count of each word in the input file. The output from the `reducer.py` script is a list of the `k` most popular words and their counts.

4. `> output_50MB.txt`: This command redirects the standard output of the `reducer.py` script to a file named `output_50MB.txt`. The file will contain the list of the `k` most popular words and their counts.

## To create stats and output File
```yaml
filename="small_50MB_dataset.txt"
output_filename=output_"${filename%.*}.txt"
if [[ -f stats.csv && $(head -n 1 stats.csv) == "Execution date,Execution time,Filename,Run elapsed time(s),CPU time user-mode(s),CPU time kernel(s),Memory usage(KB)" ]]
then
    /usr/bin/time -f "$(date +'%D,%T'),${filename},%e,%U,%S,%M" \
    bash -c "python3 mapper.py ${filename} | sort | python3 reducer.py > ${output_filename}" 2>&1 | tee -a stats.csv
else
    echo "Execution date,Execution time,Filename,Run elapsed time(s),CPU time user-mode(s),CPU time kernel(s),Memory usage(KB)" > stats.csv
    /usr/bin/time -f "$(date +'%D,%T'),${filename},%e,%U,%S,%M" \
    bash -c "python3 mapper.py ${filename} | sort | python3 reducer.py > ${output_filename}" 2>&1 | tee -a stats.csv
fi
```
* `filename="small_50MB_dataset.txt"` - This sets the variable filename to the value `"small_50MB_dataset.txt"`.
* `output_filename=output_"${filename%.*}.txt" `- This sets the variable output_filename to the value `"output_small_50MB_dataset.txt"` by using parameter expansion to remove the extension from filename and append it to the string `"output_"`.
* `if [[ -f stats.csv && $(head -n 1 stats.csv) == "Execution date,Execution time,Filename,Run elapsed time(s),CPU time user-mode(s),CPU time kernel(s),Memory usage(KB)" ]] `- This is an if statement that checks whether the file "stats.csv" exists and whether the first line of that file matches the expected header. If both conditions are true, the code inside the then block is executed; otherwise, the code inside the else block is executed.
* `/usr/bin/time -f "$(date +'%D,%T'),${filename},%e,%U,%S,%M" bash -c "python3 mapper.py ${filename} | sort | python3 reducer.py > ${output_filename}" 2>&1 | tee -a stats.csv `- This runs the command to execute the map-reduce job and time it, using the time command to measure resource usage. The output is piped to `tee`, which writes it to both the console and the `"stats.csv"` file. The format string for time includes the current date and time, the input filename, and the resource usage statistics. The map-reduce job is executed by running the mapper.py script with the input filename as an argument, sorting the output, and then running the reducer.py script to produce the final output in the output_filename file.
* `echo "Execution date,Execution time,Filename,Run elapsed time(s),CPU time user-mode(s),CPU time kernel(s),Memory usage(KB)" > stats.csv` - If the "stats.csv" file does not exist or does not have the expected header, this line creates a new file and writes the header to it.