from selenium import webdriver
from bs4 import BeautifulSoup

driver =  webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://www.youtube.com/c/Owlsreview/videos')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('#video-title')
links = soup.find_all('a', id='video-title')

f = open("C:\\Users\\User\\Desktop\\ddolddol\\Review-Filmer\\linklist.txt", "w", encoding='utf-8')

for n in titles:
    f.write(n.text.strip())

for l in links:
    f.write('youtube.com' + l.get('href'))

f.close