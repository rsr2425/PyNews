#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sqlalchemy as sa

from newspapers import get_article


user_article = None
ans = ''

print("*"*20)
print("WELCOME TO PYNEWS")
print("Here's what we recommend for you today...\n")

# prompt user to respond or request a new article
next = True
while next:
    user_article = get_article()
    print(('*' * 5) + 'ARTICLE' + ('*' * 5) + '\n\n')
    print(user_article)
    print("Input 'N' to read another article, or just hit enter to quit.")
    print("Input 'SAVE' to save the article link!")
    print('Response: ', end='')
    ans = raw_input()
    if ans == 'SAVE':
        file = open('urls.txt','a')
        file.write(user_article.url + '\n')
        file.close()
    elif ans != 'N':
        next = False

# store user response
# maybe add date?
# maybe add this to a database?
if ans != "":
    file = open('responses.txt','a')
    file.write(user_article.title + '\n')
    file.write(ans + '\n\n')
    file.close()
