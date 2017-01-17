#!/usr/bin/env python
# Name : Botspam v.0.1
# Author: mirfansulaiman
# Indonesian Backtrack Team | Kurawa In Disorder 
# http://indonesianbacktrack.or.id
# http://mirfansulaiman.com/
# http://ctfs.me/
#
# have a bug? report to doctorgombal@gmail.com or PM at http://indonesianbacktrack.or.id/forum/user-10440.html
#
# Note : This tool for education only. 
# Dont change author name !
import requests
from random import randint, choice
from string import ascii_uppercase
import string, sys, os, time
RED = "\033[1;31;40m"
WHITE = "\033[1;37;40m"
GREEN = "\033[1;32;40m"
CYAN = "\033[1;36;40m"
PURPLE = "\033[1;35;40m"
TAG = "\033[0m"

def Wordlist(listWordlist):
    if listWordlist == 'post1':
       Word = '2.txt'
    elif listWordlist == 'post2':
       Word = '4.txt'
    elif listWordlist == 'single':
       Word = '1.txt'
    else :
       Word = ''
       print "INVALID WORDLIST"
    return Word

def Post1():
    ListPost1 = open(Wordlist('post1'), "r")
    Content = ListPost1.read().splitlines()
    return Content

def Post2():
    ListPost2 = open(Wordlist('post2'), "r")
    Content = ListPost2.read().splitlines()
    return Content

def Single():
    ListSingle = open(Wordlist('single'), "r")
    Content = ListSingle.read().splitlines()
    return Content

def Telpon():
    random = randint(0,12)
    return random

def KTP():
    random = randint(0,16)
    return random

def main():
    count = 0
    for ListPost2 in Post2():
        for ListPost1 in Post1():
            for ListSingle in Single():
                url = "http://www.target.com"
                Nama = ListPost1 + ListPost2
                Email = ListPost2 + ListSingle + "@email.com"
                payload = {
                          "email":Email,
                          "nama":Nama,
                          "submit":"",
                }
                headers = {}
                timeout = 15
                try:
                   response = requests.request("POST", url, data=payload, headers=headers)
                   time.sleep(0.5)
                   count = count + 1
                   print "{0}NO{1} : {2} | {3}[SPAM REGISTER]{4}".format(WHITE, TAG, count, RED, TAG)
                   print "{0}SEND{1} : {2}{3}{4} | {5}{6}{7} ".format(WHITE, TAG, CYAN, Nama, TAG, PURPLE, Email, TAG)
                   print "{0}STATUS{1} : {2}".format(WHITE, TAG,response.text)
                
                except:
                   print "{0}NO{1} : {2} | {3}[SPAM REGISTER]{4}".format(WHITE, TAG, count, RED, TAG)
                   print "{0}SEND{1} : {2}{3}{4} | {5}{6}{7} ".format(WHITE, TAG, CYAN, Nama, TAG, PURPLE, Email, TAG)
                   print "%s[FAIL]%s : %s 404 Error %s \n" % (RED, TAG, RED, TAG)
                   print "{0}STATUS{1} : {2}".format(WHITE, TAG,response.text)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ' [Exit]'
        try:
          sys.exit(0)
        except SystemExit:
          os._exit(0)