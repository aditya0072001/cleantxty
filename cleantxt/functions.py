import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string
import re

def remove_link(text):
    filtered = re.sub(r'http\S+', '', text)

    return filtered

def remove_extra_white_space(text):
    filtered = re.sub("\s\s+" , " ", text)

    return filtered

def lower_text(text):
    return text.lower()

def upper_text(text):
    return text.upper()

def remove_stopwords(text):
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
    filtered_sentence = []
  
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    
    return ' '.join(filtered_sentence)

def remove_digits(text):
    cleaned = re.sub(r"$\d+\W+|\b\d+\b|\W+\d+$", "", text)

    return cleaned

def remove_punctuations(text):
    cleaned = text.translate(str.maketrans('', '', string.punctuation))

    return cleaned

def custom_regex(text,regex):
    cleaned = re.sub(regex, text)

    return cleaned

def stem_text(text):
    ps = PorterStemmer()
    words = word_tokenize(text)
    cleaned_words = []

    for w in words:
        cleaned_words.append(ps.stem(w))

    return ' '.join(cleaned_words)
    
def clean(text,default_case="lower",regex=None):
    try:
        cleaned = str(text)

        cleaned = remove_link(text)

        cleaned = remove_extra_white_space(cleaned)

        cleaned = remove_stopwords(cleaned)

        cleaned = remove_digits(cleaned)
        
        cleaned = remove_punctuations(cleaned)

        cleaned = stem_text(cleaned)

        if default_case == "lower":
            cleaned = lower_text(cleaned)
        else:
            cleaned = upper_text(cleaned)

        if regex:
            cleaned = custom_regex(text=text,regex=regex)

        return cleaned

    except Exception as e:
        return e

def clean_words(text,default_case="lower",regex=None):
    try:
        cleaned = str(text)

        cleaned = remove_link(text)

        cleaned = remove_extra_white_space(cleaned)

        cleaned = remove_stopwords(cleaned)

        cleaned = remove_digits(cleaned)
        
        cleaned = remove_punctuations(cleaned)

        cleaned = stem_text(cleaned)

        if default_case == "lower":
            cleaned = lower_text(cleaned)
        else:
            cleaned = upper_text(cleaned)

        if regex:
            cleaned = custom_regex(text=text,regex=regex)

        return word_tokenize(cleaned)

    except Exception as e:
        return e   
    

