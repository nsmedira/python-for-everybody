# write a Python program similar to http://www.py4e.com/code3/urllink2.py

# The program will use urllib to read the HTML from the data files: comments_42.html, comments_455223.html
from urllib.request import urlopen

from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# hard code the URL (sample data)
# The file is a table of names and comment counts
# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_455223.html'

# The program will use urllib to read the HTML from the data files: comments_42.html, comments_455223.html
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# parse the data
# Retrieve all of the span tags
tags = soup('span')

# create variable for the sum of the integer values
total = 0

# pull out the text content of the span tag
for tag in tags:

    # Look at the parts of a tag
    # extract the numbers
    # convert them to integers and add them up to complete the assignment.
    # compute the sum of the numbers in the file
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    total += int(tag.contents[0])

print(total)