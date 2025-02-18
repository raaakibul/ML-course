import requests
from bs4 import BeautifulSoup

url = 'https://www.coursera.org/'
r = requests.get(url)
# print(r.status_code)
# print(r.text)
# print(r.content)
# soup = BeautifulSoup(r.text, "lxml")
# print(soup)