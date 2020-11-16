# Pull all of the URL Links that go to the posts through the API
# Fliter out the rest of the links
# Must pull URL that links directly to each  post
# Convert each link into a page title 
# Grab the URL and then convert the title text into the functional title 
# Including capitalization and punctuation


# HINTS
# LIBRARIES TO USE
# -requests
# -inflection
# -beautiful soup

# pip install requests
# pip install inflection
# pip install beatufiulsoup4


import requests
from bs4 import BeautifulSoup
from inflection import titleize



def titles_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))

    return titles

r = requests.get('http://www.dailysmarty.com/topics/python')
soup =  BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')

titles = (titles_generator(links))

for title in titles: 
    print(title)

