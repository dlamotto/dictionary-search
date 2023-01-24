
# Dictionary Search

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/dlamotto/dictionary-search)


The project is a Python script that takes a text file as input, creates a dictionary of the string values in the text file, and then uses user input to search for specific strings. 


## Features

- The script reads the text file line by line, adding each string from each line as a key to the dictionary and the corresponding line number as its value. 
- The script then requests user input for either one or two strings to search for and uses the dictionary to find the line numbers where all of the strings appear and where any of the strings appear in the text file. 
- The script returns the line of the text file that all of the strings had appeared and the line of the text file that any of the words appeared. 


## Installation

Install dictionary_search with pip

```bash
  pip install dictionary_search
```
    
## Examples

```bash
$ python -m dictionary_search
#or
$ dictionary_search

```
```python
from dictionary_search import user_input_question()

user_input_question()

```
