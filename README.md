# Map-Reduce-K-Most-Popular-words

## To run mapper separately
`python3 mapper.py small_50MB_dataset.txt > intermediate_data.txt`

## To run reducer separately after mapper
`cat intermediate_data.txt | sort | python3 reducer.py`

## To run on local system
`python3 mapper.py small_50MB_dataset.txt | sort | python3 reducer.py`
