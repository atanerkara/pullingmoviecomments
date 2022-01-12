from selenium import webdriver
from bs4 import BeautifulSoup
import time


burp0_url = "https://www.beyazperde.com/filmler/film-275065/kullanici-elestirileri/"
browser = webdriver.Chrome(executable_path="C:\\Users\\Ahmet Taner\\prog\\chromedriver.exe")
browser.get(burp0_url)
time.sleep(2)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find_all("a", {"class": "xXx button button-md item"})
sayi = 0
time.sleep(2)
for i in temp:
    a = i.text
time.sleep(2)
commentfile = open("comments.txt",'w+', encoding="iso8859_9")
iiyorumsayisi = 0
kotuyorumsayisi = 0
for i in range(int(a)):
    browser.get(burp0_url + "?page=" + str(i+1))
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    comments = soup.find_all("div", {"class": "content-txt review-card-content"})
    for comment in comments:
        comment = comment.text
        print(comment)
        print("\n")
        sayi += 1
        commentfile.write(comment.encode(encoding='iso8859_9', errors='ignore').decode('iso8859_9')) #because of emojis in comments
commentfile.close()
print(sayi)
time.sleep(2)
browser.close()
