#! /Users/stephenlang/anaconda/bin/python
#LinkVerification is a program that, given the URL of a web page, will attempt to down- 
# load every linked page on the page.The program will flag any pages that have a 404 
# “Not Found” status code and print them out as broken links.

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sys, requests, os
from urllib.parse import urljoin

#take in a web address
url = 'http://' + sys.argv[1]

#go to that web address
#find all links on the page
ua = UserAgent()

def lovely_soup(url):
    r = requests.get(url, headers={'User-Agent': ua.chrome})
    return BeautifulSoup(r.text,'lxml')

soup = lovely_soup(url)

links = soup.select('a')

for link in links:
    ck_url = urljoin(url, link.get('href'))
    print('Checking the status of' + ck_url,end=" ")

    try:
       res = requests.get(ck_url, headers={'User-Agent': ua.chrome})
    except requests.exceptions.InvalidSchema as ma:
       print('Error:'+ ma)

    try:
        res.raise_for_status()
        print('Status Ok')
    except:
        print('Error %s occurred' % res.status_code())
