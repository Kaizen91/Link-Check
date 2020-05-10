#! /Users/stephenlang/anaconda/bin/python
#LinkVerification is a program that, given the URL of a web page, will attempt to down- 
# load every linked page on the page.The program will flag any pages that have a 404 
# “Not Found” status code and print them out as broken links.

import sys, bs4, requests
#take in a web address



#go to that web address

#find all links on the page

#iterate through all the links finding all subsequent links