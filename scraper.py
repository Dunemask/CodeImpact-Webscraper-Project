#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
site='http://www.dailysmarty.com/topics/python'
r = requests.get(site)
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
posts = genPosts(links)
def genPosts(links):
    posts = []
    for link in links:
        if link.get('href') == None:
            continue
        else:
            if "post" in link.get('href'):
                posts.append(link.string)
            elif "post" in link.get('href') and link.string==None:
                posts.append("Posts")

    return posts
for post in posts:
    print(post)
