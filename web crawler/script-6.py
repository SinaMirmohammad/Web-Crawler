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
#del f1
#static_url = urls
#del urls
#del grab
#del soup
#--------------------------------------
#Count URLs List
Counter_list_0 = 0
f2 = open("Step_1_urls.txt", "r")
Content_0 = f2.read() 
CoList_0 = Content_0.split("\n")
  
for i in CoList_0: 
    if i: 
        Counter_list_0 += 1
f2.close
print("URL Count in index page ==> ", Counter_list_0)
Counter_list_0 = 10

del f2
del Content_0
del CoList_0

#--------------------------------------
#Step_2
f3_r = open("Step_1_urls.txt", "r")

for Round_i_0 in range(Counter_list_0 + 1):
    f3_w = open("Step_1_urls.txt", "a+")
    indexline_step_1 = f3_r.readline()
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

    Counter_list_0 = 0
    f4 = open("Step_1_urls.txt", "r")
    Content_0 = f4.read() 
    CoList_0 = Content_0.split("\n")
    
    for i in CoList_0: 
        if i: 
            Counter_list_0 += 1
    f4.close
    print("URL Count in index page ==> ", Counter_list_0)

    f3_w.close()
    print(Round_i_0 ,"<------> ", "\n")
    Round_i_0 += 1

f3_r.close()
