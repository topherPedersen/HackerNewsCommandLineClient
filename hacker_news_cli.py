# REFERENCE (python requests): https://realpython.com/python-requests/
# REFERENCE (Hacker News API): https://github.com/HackerNews/API

from lxml import html
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

top_stories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
top_stories_str = top_stories.text
top_stories_json = top_stories.json()

# https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty
url = 'https://hacker-news.firebaseio.com/v0/item/' + str(top_stories_json[0]) + '.json?print=pretty'
story = requests.get(url)
story_json = story.json()
story_url = story_json['url']


story_html = requests.get(story_url).content
# response = urlopen(story_url)
# story_html = response.read().decode(encoding="unicode")

story_beautiful_soup = BeautifulSoup(story_html, 'html.parser')

ptag = story_beautiful_soup.find_all('p')
for p in ptag:
    paragraph_length = len(p.text)
    line = [] # create array to hold individual lines of text
    line.append("")
    i = 0 # i keeps track of characters in paragraph
    j = 0 # j keeps track of characters in individual lines
    k = 0 # k keeps track of number of lines per paragraph
    while i < paragraph_length:
        line[k] = line[k] + p.text[i] 
        i = i + 1
        if j < 80:
            j = j + 1
        else: 
            j = 0
            k = k + 1
            line.append("") # append new string for new line to list

    for line in line:
        print(line)
    print("")
    # print(p.text)
