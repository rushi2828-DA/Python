import requests
from bs4 import BeautifulSoup
import selenium as sn
import scrapy as sp


#url to scrape
url='http://www.vulnweb.com/'
#send an HTTPS GET request 
response=requests.get(url)

#check if the request was successfully 
if response.status_code==200:
    #parse the HTML content
    soup=BeautifulSoup(response.text,'html.parser')

#find all heading tags
for heading in soup.find_all(['h1','h2','h3','h4','h5','h6']):
    print(heading.text.strip())
else:
    print(f'failed to retrieve the page.statuscode:{response.status_code}')

