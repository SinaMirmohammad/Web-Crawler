#Coding By SinaMirmohammad
#!usr/bin/env python
#Find URL & Crwl in Domain

import requests
from bs4 import BeautifulSoup
 
urls = str(input("Enter Domain ==> "))
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
#--------------------------------------
#Step_1
# opening a file in write mode
f1 = open("Step_1_urls.txt", "w")
f1.truncate(0)
# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   data = str(data)
   if data[0] == "/":
       data = str(urls) + data
   f1.write(data + "\n")
   del data
 
f1.close()
#--------------------------------------
f3_r = open("Step_1_urls.txt", "r")
a = 1
while True:
    f3_w = open("Step_1_urls.txt", "a+")
    a += 1
    indexline_step_1 = f3_r.readline()
    print(a,">>> ",indexline_step_1, "\n")
    if not(indexline_step_1.find(urls) == -1):
        grab = requests.get(indexline_step_1)
        soup = BeautifulSoup(grab.text, 'html.parser')
        for link in soup.find_all("a"):
            data = link.get('href')
            data = str(data)
            if data[0] == "/":
                data = str(urls) + data
            f3_w.write(data + "\n")
    elif indexline_step_1[0] == "/":
        indexline_step_1 = str(urls) + indexline_step_1
        grab = requests.get(indexline_step_1)
        soup = BeautifulSoup(grab.text, 'html.parser')
        for link in soup.find_all("a"):
            data = link.get('href')
            data = str(data)
            if data[0] == "/":
                data = str(urls) + data
            f3_w.write(data + "\n")
    
    f3_w.close()

f3_r.close()
