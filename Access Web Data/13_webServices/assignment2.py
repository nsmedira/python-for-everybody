# write a Python program somewhat similar to http://www.py4e.com/code3/json2.py

import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# prompt for a URL
address = input('Enter location: ')

# read the JSON data from that URL using urllib
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()



# parse and extract the comment counts from the JSON data
comments = json.loads(data)['comments']

# compute the sum of the numbers in the file
total = 0
for line in comments :
    total += line['count']

# for item in info:
    # print('Name', item['name'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])

print(total)