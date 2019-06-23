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

story_content = []
story_title = []
story_count = 0
story_link = []
for id in top_stories_json:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json?print=pretty'
    story = requests.get(url)
    story_json = story.json()
    # print(story_json['title'])
    story_title.append(story_json['title'])
    try:
        story_url = story_json['url']
        story_link.append(story_url)
        story_html = requests.get(story_url).content
        story_content.append(story_html)
    except:
        story_content.append("nothing to see here, sorry")
    print("loading...")
    # story_title.append(story_json['title'])
    # print(id)
    story_count = story_count + 1
    if story_count >= 5:
        break

'''
for title in story_title:
    print(title)
    print("")
'''

def show_titles():
    global story_title
    for title in story_title:
        print(story_title)

def show_story(raw_html):
    story_beautiful_soup = BeautifulSoup(raw_html, 'html.parser')

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

def select_story(selection):
    global story_content
    show_story(story_content[selection])

i = 0
for title in story_title:
    print(str(i) + ": " + title)
    i = i + 1

story_selected = input("Select Story To Read: ")
story_selected = int(story_selected)
select_story(story_selected)
