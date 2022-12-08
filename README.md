# cleantxty
[![Downloads](https://pepy.tech/badge/cleantxty/month)](https://pepy.tech/project/cleantxty)
Python package to clean strings and making them reasonable for NLP.

**cleantxty** is a an open-source python package cleaning text from raw text format. Source code for the library can be found [here.](https://github.com/aditya0072001/cleantxty)



## Features 

cleantxt has two main methods,
* **clean**: to clean raw text and return the cleaned text
* **clean_words**: to clean raw text and return a list of clean words

other menthods that can be used simultaneoulsy are:
* **remove_link**: to remove link from the text
* **remove_extra_white_space**: to remove extra white space from the text
* **lower_text**: to make case of the text to lower case
* **upper_text**: to make case of the text to upper case
* **remove_stopwords**: to remove stopwords from the text
* **remove_digits**: to remove digits from the text
* **remove_punctuations**: to remove punctuations from the text
* **custom_regex**: to use custom regex and appy to text
* **stem_text**: to stem the provided text


## Installation

cleantext requires [Python 3](https://www.python.org/downloads/) and [NLTK](http://www.nltk.org/install.html) to execute. 

To install using pip, use

`pip install cleantxty`

## Usage

* **Import the library**:

``` python
import cleantxty
```

* **Choose a method:**

 To return the text in a string format, 
 
``` python
cleantxty.clean("raw_text_here") 
```
 
 To return a list of words from the text,
 
``` python
cleantxty.clean_words("raw_text_here") 
```
 
 To choose a specific set of cleaning operations,

``` python
cleantxty.clean("raw_text_here",
default_case= "lower", # lower by default change to upper for upper case result
regex=None  # Provide custom regex to use
)

cleantxty.clean_words("raw_text_here",
default_case= "lower", # lower by default change to upper for upper case result
regex=None  # Provide custom regex to use
)
```

## Examples

``` python
import cleantxty
cleantxty.clean('This is A s$ple ? tExt3% to   cleaN566556+wow8 ')
```

returns,

``` Python
'this is a sample text to clean'
```

----

``` Python
import cleantxty
cleantext.clean_words('This is A s$ample !!!! tExt3% to   cleaN566556+2+59*/133')
```

returns,

``` Python
['sampl', 'text', 'clean']
```

----

``` Python
from cleantxty import clean
text = "my id, name1@dom1.com and your, name2@dom2.in"
clean(text, regex=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
```

returns,

``` Python
"my id, email and your, email"
```

## License

##### MIT

For any questions, issues, bugs, and suggestions please visit [here](https://github.com/aditya0072001/cleantxt/issues)