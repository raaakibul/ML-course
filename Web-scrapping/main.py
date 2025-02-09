import requests

url = 'https://www.coursera.org/'
r = requests.get(url)
# print(r.status_code)
print(r.text)