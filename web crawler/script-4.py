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
   f1.write(data + "\n")
   #f1.write("\n")
   del data
 
f1.close()
del f1
static_url = urls
del urls
del grab
del soup
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
print("URL Count 0 ==> ", Counter_list_0)
del f2
del Content_0
del CoList_0

#--------------------------------------
#Step_2
f3_r = open("Step_1_urls.txt", "r")
f3_w = open("Step_1_urls.txt", "w")

for Round_i_0 in range(0,Counter_list_0 + 1):

    indexline_step_1 = f3_r.readline()

    if not(indexline_step_1.find(static_url) == -1):

        grab = requests.get(indexline_step_1)
        soup = BeautifulSoup(grab.text, 'html.parser')

        for link in soup.find_all("a"):
            data = link.get('href')
            data = str(data)
            #-----------------------
            Counter_list = 0
            f4 = open("Step_1_urls.txt", "r")
            Content_0 = f4.read() 
            CoList_0 = Content_0.split("\n")
            
            for i in CoList_0: 
                if i: 
                    Counter_list_1 += 1
            f2.close
            #print("URL Count ==> ", Counter_list_1)
            f4.close()
            del f4
            del Content_0
            del CoList_0
            #-----------------------
            finder_url = ""
            for Round_i_1 in range(0,Counter_list_1 + 1):
                indexline_step_2 = f4.readline()
                if indexline_step_2.find(data) == -1:
                    finder_url = "No"
                elif not(indexline_step_2.find(data) == -1):
                    finder_url = "Yes"
                
                Round_i_1 += 1

            if finder_url == "No":
                f3_w.write(data + "\n")
            

            del finder_url
            del data

        del grab
        del soup   

    del indexline_step_1
    Round_i_0 += 1