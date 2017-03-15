import requests
from bs4 import BeautifulSoup

content = requests.get('https://movie.douban.com').content
soup = BeautifulSoup(content, 'html.parser')

for div in soup.find_all('div',{'class':'review-content'}):
    print div.text.strip()
