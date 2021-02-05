# write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    # hard code address for easier testing
    # prompt for a location
    # address = input('Enter location: ')
    address = 'Beijing normal University'

    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)

    # contact a web service
    uh = urllib.request.urlopen(url, context=ctx)

    # retrieve JSON for the web service
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    # parse that data
    # retrieve the first place_id from the JSON
    # A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
    location = js['results'][0]['place_id']
    print(location)
    break