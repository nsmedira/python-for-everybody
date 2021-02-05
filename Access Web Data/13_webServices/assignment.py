# write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# WE DO NOT NEED API KEY
# api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# DON'T CARE ABOUT API KEY
# if api_key is False:
    # api_key = 42
    # serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
    # serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    # prompt for a URL
    address = input('Enter location: ')
    if len(address) < 1: break

    # WE DON'T NEED PARAMETERS FOR THE API
    # parms = dict()
    # parms['address'] = address
    # if api_key is not False: parms['key'] = api_key
    # url = serviceurl + urllib.parse.urlencode(parms)

    # DEBUG: SHOW ADDRESS INSTEAD OF URL
    # print('Retrieving', url)
    print('Retrieving', address)

    # OPEN ADDRESS INSTEAD OF URL
    # uh = urllib.request.urlopen(url, context=ctx)
    uh = urllib.request.urlopen(address, context=ctx)

    # read the XML data from that URL using urllib
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)

    # parse and extract the comment counts from the XML data
    results = tree.findall('comments/comment')

    # compute the sum of the numbers in the file.
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
    total = 0
    for line in results :
        value = line.find('count').text
        total += int(value)
        print(value, total)

    # print('lat', lat, 'lng', lng)
    # print(location)

    # BREAK OUT OF THE WHILE LOOP
    break

# PRINT THE TOTAL
print(total)