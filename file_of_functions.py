import numpy as np
import urllib
import pandas as pd
import math
from collections import Counter
#import numpy as np
import urllib
from urllib.request import urlopen
import pandas as pd
import requests
import io
import time
import bs4 as bs
import re
import nltk
from nltk import download
from bs4 import BeautifulSoup
from string import punctuation as pnc
from nltk.corpus import stopwords
import math

from collections import Counter



def get_each_url(filepath):

    with open(filepath, "r") as f:
            # spliting the urls line by line 
        start_url_extraction = [url.split() for url in f.readlines()]
        for extract_list in start_url_extraction:
    # reading all the urls as  list from text file and extracting one by one in loop
            #for url_item  in  extract_list:
                #print(list_item)   # url we are going to soup
            return extract_list



    #finally:
    
            #return stopword_removed_text
    #return as_list_soup

    
#as_list_soup()   
#print(as_list_soup("https://en.wikipedia.org/wiki/Information_security"))


def counter_cosine_similarity(corpus, list_values):
    #corpus = c1
    #list_values = c2
    # print(listA)
    # print(listB)
    corpus_counter  = Counter(corpus)
    list_values_counter  = Counter(list_values)

    terms = set(corpus_counter).union(list_values_counter)
    dotprod = sum(corpus_counter.get(k, 0) * list_values_counter.get(k, 0) for k in terms)
    magA = math.sqrt(sum(corpus_counter.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(list_values_counter.get(k, 0)**2 for k in terms))
    #return dotprod / (magA * magB)
    denominator=(magA * magB)
    if not denominator:
        return 0.0
    else:
        return float(dotprod) / denominator


def get_corpus(each_url):
    # not_crawled=[]
    # global stopword_removed_text
    # punctuation = punctuation
    
    string = urllib.request.urlopen(each_url)

    str_from_url = string.read() 
    text = str_from_url

    article= text
    parsed_article = bs.BeautifulSoup(article,'lxml')  # BeautifulSoup is a Python library for parsing HTML and XML documents.
    # Find all the the paragraph tags and then get the text i.e; Getting the text from all p elements in a div with BeautifulSoup
    paragraphs = parsed_article.find_all('p')

    article_text = ""
    for p in paragraphs:
        article_text += p.text
    output = ''.join(c for c in article_text if not c.isdigit())

    # defining a nested function to remove punctuations from the corpus
    def strip_punctuation(s):
        return ''.join(c for c in s if c not in pnc)

    punctuation_striped=strip_punctuation(output)

    # Cleaing the text and preprocessing the text:
    processed_article9 = punctuation_striped.lower()  
    # Anything except 0..9, a..z and A..Z is replaced by space or replaced by nothing
    processed_article9= re.sub('[^a-zA-Z]', ' ', processed_article9)  
    # \s+ Matches Unicode whitespace each_urlacters, which includes [ \t\n\r\f\v], and also many other each_urlacters and replaces them with space
    processed_article9 = re.sub(r'\s+', ' ', processed_article9)  
    ## stop word removal
    stop_words = set(stopwords.words('english')) 
    words = processed_article9.split() 
    stopword_removed_text=([i for i in processed_article9.lower().split() if i not in stop_words])
    #return stopword_removed_text
    cleaned_txt_2 = stopword_removed_text
    return stopword_removed_text

    #finally:
    
            #return stopword_removed_text
    #return as_list_soup

    
#as_list_soup()   
#print(as_list_soup("https://en.wikipedia.org/wiki/Information_security"))
