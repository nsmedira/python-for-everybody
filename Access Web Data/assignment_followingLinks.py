# write a Python program that expands on http://www.py4e.com/code3/urllinks.py

# use urllib to read the HTML from the data files: http://py4e-data.dr-chuck.net/known_by_Fikret.html (sample); http://py4e-data.dr-chuck.net/known_by_Kamilia.html (actual)
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# hard code the sample URL:
# url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

# hard code the actual URL
url = 'http://py4e-data.dr-chuck.net/known_by_Kamilia.html'

# start a counter
count = 0

# SAMPLE - go to the 3rd link on the webpage 4 times
# ACTUAL - go to the 18th link on the webpage 7 times
index = 17
while count < 7 :

    # follow that link
    html = urllib.request.urlopen(url, context=ctx).read()

    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')

    # create a list of the links
    links = list()
    names = list()

    # extract the href= vaues and the names from the anchor tags
    for tag in tags:
        names.append(tag.contents[0])
        links.append(tag.get('href', None))

    # scan for a tag that is in a particular position relative to the first name in the list
    # SAMPLE - get the third name in the list
    url = links[index]

    # increment the counter
    count += 1

# report the last name you find
print(names[index])