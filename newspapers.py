#!/usr/bin/python
# _*_ coding:utf-8 _*_

# python module to handle obtaining newspaper articles and obtaining the text

import string
from random import randint

import requests
from bs4 import BeautifulSoup

# right now the code only works for nytimes
url = 'http://www.nytimes.com/'

class Article(object):
    def __init__(self, title, url, text):
        self.title = title
        self.url = url
        self.text = text

    def __str__(self):
        return(self.title + '\n\n' + self.url + '\n\n' + self.text)
    
def _download_articles():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup.findAll('article')

def _clean_string(a_string):
    a_string = a_string.replace('\n\n\n', '\nn')
    a_string = a_string.replace('\n\n','\n')
    a_string = a_string.replace('Advertisement', '')

    printable = set(string.printable)
    a_string = filter(lambda x: x in printable, a_string)
    return a_string

def _clean_article(article_soup, url):
    printable = set(string.printable)

    # occassionally the article titles return characters that can't be encoded
    # to account for this, filter out the non-ascii chars for now
    article_title = article_soup.findAll("h1", {'class' : 'headline'})[0].get_text()
    article_title = _clean_string(article_title)
    
    text = ''
    for paragraph_html in article_soup.findAll("div", { "class" : "story-body" }):
        paragraph_soup = BeautifulSoup(str(paragraph_html), 'lxml')

        # clean up tags from article
        paragraphs = paragraph_soup.findAll("p")
        for p in paragraphs:
            p = p.get_text()
            text += (p + '\n')

    # clean up text
    text = _clean_string(text)
            
    return Article(article_title, url, text)
    
    
def select_article(articles):
    article_num = len(articles)
    an_article = articles[randint(0, article_num - 1)]
    url = an_article.findAll('a', href=True)[0]['href']
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    return _clean_article(soup, url)
    

def get_article():
    articles = _download_articles()
    user_article = select_article(articles)

    return user_article
