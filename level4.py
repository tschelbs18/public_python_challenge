# use URLLIB python module or requests
# looks like I'll need to follow multiple levels of URLS to get to the end of the chain programmatically

import urllib
import requests

def fn_continue():
    cont_bool = input("would you like to continue (y/n): ")
    if cont_bool[0].lower() == 'y':
        return True
    else:
        return False
        
def edit_url(test_url):
    edit_bool = input("would you like to edit the test url (y/n): ")
    if edit_bool[0].lower() == 'y':
        new_url = input("enter the new test url (just number): ")
        return 'linkedlist.php?nothing=' + new_url
    else:
        return test_url
        
found_end = False

r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
test_url = '12345'
print(r.text)
print(r.text[r.text.find('<a href="') + 9: r.text.find('>',r.text.find('<a href=') + 8)-1])
counter = 0

while found_end == False:
    counter += 1
    r = requests.get(base_url + test_url)
    #test_url = r.text[r.text.find('<a href="') + 9: r.text.find('>',r.text.find('<a href=') + 8)-1]
    print(r.text)
    test_url = r.text[r.text.find(' is ') + 4:]
    print("Going to try this url: " + test_url)
    #test_url = edit_url(test_url)
    #if not(fn_continue()):
    #   found_end = True
    if not('and the next nothing is' in r.text):
        print('Not the normal format')
        test_url = edit_url(test_url)
    if counter > 500:
        found_end = True
        
    #Stops at peak.html
