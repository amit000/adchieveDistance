# read addresses-----done
# bulk query only for longitude lattitude----can't do bulk query in free tier
# query one by one---done
# add long lat to obj
# design function to calculate distance using long lat
# find out source long latt
# find out distance between source and every other address, add distance to the obj/dict
# sort objs/dicts by distance
# print in format

import http.client, urllib.parse
import locations

locs = locations.create_location_list("addresses.txt")

conn = http.client.HTTPConnection('api.positionstack.com')

YOUR_ACCESS_KEY = ""
for loc in locs:
    params = urllib.parse.urlencode({
        'access_key': YOUR_ACCESS_KEY,
        'query': loc.address,
        'fields': 'results.latitude',
        'limit': 1,
    })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    print(data.decode('utf-8'))
    loc.
