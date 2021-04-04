#Coding By SinaMirmohammad
#!usr/bin/env python
#Coding By SinaMirmohammad
#!usr/bin/env python
import requests
from bs4 import BeautifulSoup
 
urls = str(input("Please input url ==> "))
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
 
# opening a file in write mode
f1 = open("test1.txt", "w")
f1.truncate(0)
# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   data = str(data)
   f1.write(data)
   f1.write("\n")
   #f1.write("\n")

f1.close()

