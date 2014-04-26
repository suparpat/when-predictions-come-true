__author__ = 'maud'
import nltk
from nltk.corpus import stopwords
import re

CUSTOM_STOPWORDS = ["AT_USER", "URL"]
INV = ["lack of", "not", "n't"]

def preprocess(text):


    nb_exclamations_mark = text.count("!")
    nb_capital_letter = sum(x.isupper() for x in text)
    text = text.lower()
    text = re.sub('((www\.[\s]+)|(https?://[^\s]+))', 'URL', text)
    text = re.sub('@[^\s]+', 'AT_USER', text)
    text = re.sub(r'#([^\s]+)', r'\1', text)
    text = text.strip('\'"')
    for invert in INV:
        if invert in text:
            inv = True
        else:
            inv = False
    words = text.split()
    stopset = getStopWords()
    words_feature = []
    for word in words:
        word = replaceTwoOrMore(words)
        word = word.strip('\'"?,.')
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)
        if word in stopset or val is None:
            continue
        else:
            words_feature.append(word.lower())

    return nb_capital_letter, nb_exclamations_mark, words_feature, inv


def replaceTwoOrMore(text):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", text)

def getStopWords():
    stopset = stopwords.words('english')
    for custom in CUSTOM_STOPWORDS:
        stopset.append(custom)
    return stopset