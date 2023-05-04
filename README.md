# Map-Reduce-K-Most-Popular-words

## To run mapper separately
`cat small_50MB_dataset.txt | python3 mapper.py > mapped_data.txt`
> reads the contents of the `small_50MB_dataset.txt` file, passes it as input to the `mapper.py` script using the `cat` command, and then writes the output to a new file called `mapped_data.txt`.

## To run reducer separately after mapper
`cat mapped_data.txt | sort | python3 reducer.py > reduced_data.txt`
> reads the contents of the `mapped_data.txt` file, sorts it using the `sort` command (because the reducer requires sorted input), passes it as input to the `reducer.py` script using the `cat` command, and then writes the output to a new file called `reduced_data.txt`.

## To run reducer_topk after mapper, and reducer
`cat reduced_data.txt | python3 reducer_topk.py 100 > top_k.txt`
> reads the contents of the `reduced_data.txt` file, passes it as input to the `reducer_topk.py` script using the `cat` command, and then writes the output to a new file called `top_k.txt`.

## To run all the three programs in one command line
`cat small_50MB_dataset.txt | python3 mapper.py | sort | python3 reducer.py | python3 reducer_topk.py 100 > top_k.txt`

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
