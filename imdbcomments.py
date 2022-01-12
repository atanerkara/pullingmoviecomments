from selenium import webdriver
from bs4 import BeautifulSoup
import time

burp0_url = "https://www.imdb.com/title/tt10872600/reviews?ref_=tt_urv"
browser = webdriver.Chrome(executable_path="C:\\Users\\Ahmet Taner\\prog\\chromedriver.exe")

browser.get(burp0_url)
time.sleep(2)
browser.find_element_by_id("load-more-trigger").click()
time.sleep(2)
browser.find_element_by_id("load-more-trigger").click()
time.sleep(2)
browser.find_element_by_id("load-more-trigger").click()
time.sleep(2)
browser.find_element_by_id("load-more-trigger").click()
time.sleep(2)
browser.find_element_by_id("load-more-trigger").click()
html = browser.page_source
time.sleep(2)
i=0
browser.close()
soup = BeautifulSoup(html, 'html.parser')
comments = soup.find_all("div", {"class": "text show-more__control"})#.get('text')
for comment in comments:
    comment = comment.text
    i+=1
print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL\n",len(comment),i)
