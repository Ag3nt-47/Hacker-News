import requests
from bs4 import BeautifulSoup
import threading

response = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(response.text, 'html.parser')
tag = soup.find_all('a')
news_id_list = []

for link in tag:
    found = link.get('href')
    if found.startswith('item?id='):
        news_id_list.append(found)

news_id_list = list(set(news_id_list))

counter = 1

for id in news_id_list:
    id = id.strip('=')[8:]
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
    link = response.json().get('url')
    if link != None:
        print(f"news {counter}: {link}")
        counter += 1
    else:
        text = response.json().get('text')
        print(f"news {counter}: {text}")
        counter+=1
