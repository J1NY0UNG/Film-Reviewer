from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.naver.com/")

bsObject = BeautifulSoup(html, "html.parser")

f = open("C:\\Users\\User\\Desktop\\ddolddol\\project\\dashspace\\cinema-reviewer\\linklist.txt" , 'w')

for link in bsObject.find_all('a'):
    print(link.get('href'))

