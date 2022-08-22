from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.youtube.com/c/Owlsreview/videos")

bsObject = BeautifulSoup(html, "html.parser")

f = open("C:\\Users\\User\\Desktop\\ddolddol\\Review-Filmer\\linklist.txt" , 'w')

for link in bsObject.find_all('a'):
    f.write(link.get('href'))

f.close