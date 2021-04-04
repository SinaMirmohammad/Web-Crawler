#Coding By SinaMirmohammad
#!usr/bin/env python
#Find URL & Crwl in Domain

import requests
from bs4 import BeautifulSoup
 
urls = "https://www.google.com"
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
 
# opening a file in write mode
f1 = open("urls_raw.txt", "w")
f1.truncate(0)
# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   f1.write(data + "\n")
   #f1.write("\n")
   del data
 
f1.close()
del urls
del grab
del soup

#----------------------------------------------
#Count URLs List
Counter_list = 0
f2 = open("urls_raw.txt", "r")
Content_2 = f2.read() 
CoList_2 = Content_2.split("\n")
  
for i in CoList_2: 
    if i: 
        Counter_list += 1
f2.close
print("URL Count ==> ", Counter_list)
del f2
#----------------------------------------------
f3 = open("urls_raw.txt", "r")
f4 = open("urls_pars.txt", "w")
f4.truncate(0)
for Round_i_0 in range(0,Counter_list + 1):
    
    buffer_url = f3.readline()
    find_domain = buffer_url.find("https://www.google.com")
    if not(find_domain == -1):
        print("=" * 30)
        print(buffer_url, "\n")
        #print("Round Requests ==>", Round_i_0, "\n")
        print("=" * 30)
        grab = requests.get(buffer_url)
        soup = BeautifulSoup(grab.text, 'html.parser')
        for link in soup.find_all("a"):
            data = link.get('href')
            data = str(data)
            
            #Count URL pars
            Counter_list_pars = 0
            f2 = open("urls_pars.txt", "r")
            Content_2 = f2.read() 
            CoList_2 = Content_2.split("\n")
            
            for i in CoList_2: 
                if i: 
                    Counter_list_pars += 1
            f2.close
            #print("URL Pars Count ==> ", Counter_list_pars)
            f5 = open("urls_pars.txt", "w")
            for Round_i_pars in range(0,Counter_list_pars):
                read_pars = f5.readline().find(data)
                if read_pars == -1:
                    f4.write(data + "\n")
            del data

        del buffer_url
        del grab
        del soup

        #f4.close()
        Round_i_0 += 1
