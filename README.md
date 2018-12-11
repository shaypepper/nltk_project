# Shay's Text Processing

## Getting started

### Downloading project
If you don't have the zip file for this project, you can clone it from github if you have it. 
```{bash}
$ git clone https://github.com/shaypepper/shay_eigen_project.git
```

### Conda 

If you don't have conda on your machine, you can download Miniconda for your machine [here](https://conda.io/miniconda.html).

Make sure you have the most recent version of Conda. (Even if you just installed it!)

```{python}
$ conda update conda
$ conda env create --name shay_eigen --file text_process.yml
$ source activate shay_eigen
```

### NLTK
The NLTK library requires a couple of downloads through its interface (as opposed to Conda). You'll need to download these as well. I have a script for you to do this quickly.
```{python}
$ python get_nltk_packages.py
```

### Example
In order to test, you will go in the the python shell. I'll provide a few start lines to show you the output from the data provided. You can look at the docs below to get an idea of other functionality. These commands should be from within the project directory. 

```{python}
$ python
>>> from text_process import *
>>> c = Corpus(paths=TEST_PATHS, exclude=["and","i"])
>>> mcw = c.most_common_words(3, print_result = True)
```


## Classes

### ``class TextProcessor``

#### ``tp.get_token_set(doc)``

Takes doc in the form of a string and returns list of unique tokens.

#### ``tp.preprocess_string(doc)``

Takes doc in the form of a string, preprocesses data by removing tokens that aren't words and stop words. It also changes all tokens to lowercase. 

### ``class Corpus(docs=[], paths=None, language='english', exclude=[])``
This is our main class that allows you to provide docs or paths to be processed. 

   * ``docs``: a list of strings, each will be called a doc 
   * ``paths``: a list of file paths to read docs from.
   * ``language``: string. specify language to assume in removing stop words.
   * ``exclude``: list of words to exclude in addition to stop words.


#### ``corpus.most_common_words(self, n=5, range=None, print_result=False):``
This method gives you the first ``n`` of the most common words or the i to j most common words by specifying ``range=(i,j)``. It returns a list of data dictionaries with the word, documents the word is found in, and sentences the word is found in. 
Optionally, you can print the results for a nicely formatted output. 

#### ``corpus.word_data(word)``
This method takes a single word and gets the word/sentence/documents data like most_common_words. 

#### ``corpus.word_list_data(word_list)``
Just like word_data, except it takes and returns a list of word_data. 
