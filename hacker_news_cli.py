# REFERENCE (python requests): https://realpython.com/python-requests/
# REFERENCE (Hacker News API): https://github.com/HackerNews/API

print("Hacker News CLI by Topher Pedersen")
print("loading...")

from lxml import html
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

story_content = []
story_title = []
story_link = []

def get_top_stories(first_story_index, last_story_index):

    global story_content
    global story_title
    global story_count
    global story_link

    story_content = []
    story_title = []
    story_count = -1
    story_link = []

    top_stories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    top_stories_str = top_stories.text
    top_stories_json = top_stories.json()

    for id in top_stories_json:

        story_count = story_count + 1

        if story_count < first_story_index:
            continue
        elif story_count > last_story_index:
            break

        url = 'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json?print=pretty'
        story = requests.get(url)
        story_json = story.json()
        story_title.append(story_json['title'])

        try:
            story_url = story_json['url']
            story_link.append(story_url)
            story_html = requests.get(story_url).content
            story_content.append(story_html)
        except:
            story_content.append("nothing to see here, sorry")

        print("loading...")

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

def show_top_stories():
    i = 0
    for title in story_title:
        print(str(i) + ": " + title)
        i = i + 1

keep_reading = True
while keep_reading == True:

    page = input('Which page of stories would you like to view?: ')
    page = int(page)

    if page == 1:
        get_top_stories(0, 9)
    elif page == 2:
        get_top_stories(10, 19)
    elif page == 3:
        get_top_stories(20, 29)
    elif page == 4:
        get_top_stories(30, 39)
    elif page == 5:
        get_top_stories(40, 49)
    elif page == 6:
        get_top_stories(50, 59)
    elif page == 7:
        get_top_stories(60, 69)
    elif page == 8:
        get_top_stories(70, 79)
    elif page == 9:
        get_top_stories(80, 89)
    elif page == 10:
        get_top_stories(90, 99)

    show_top_stories()
    story_selected = input("Select Story To Read: ")
    story_selected = int(story_selected)
    select_story(story_selected)
    keep_reading = input('Keep reading? Enter y for yes, no for no:')

    if keep_reading == "no" or keep_reading == "n":
        keep_reading = False
    else:
        keep_reading = True
