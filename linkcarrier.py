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

for k in titles:
    f.write(k.text.strip())
    f.write("\n")

for l in links:
    f.write(l.get('href'))
    f.write("\n")

f.close