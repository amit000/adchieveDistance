# read addresses-----done
# bulk query only for longitude lattitude----can't do bulk query in free tier
# query one by one---done
# add long lat to obj--done
# design function to calculate distance using long lat---done
# find out source long latt--done
# find out distance between source and every other address obj,---done
# sort list by distance---done
# print in format---done

import asyncio
import http.client
import urllib.parse
import json
from operator import attrgetter

import locations

locs = locations.create_location_list("addresses.txt")

conn = http.client.HTTPConnection('api.positionstack.com')

YOUR_ACCESS_KEY = ""


async def get_locations(locs):
    for loc in locs:
        params = urllib.parse.urlencode({
            'access_key': YOUR_ACCESS_KEY,
            'query': loc.address,
            'fields': 'results.latitude',
            'limit': 1,
        })
        conn.request('GET', '/v1/forward?{}'.format(params))
        res = conn.getresponse()
        print(f"started for {loc.name}")
        data = res.read()
        b = json.loads(data)
        loc.add_long_lat(b)
    return locs


locs = asyncio.run(get_locations(locs))

source = None
for i, loc in enumerate(locs):
    if loc.name == "Adchieve HQ":
        source = locs.pop(i)
        break

for loc in locs:
    loc.distance_from_source(source)

locs.sort(key=attrgetter('distance'))

for i, loc in enumerate(locs):
    print(str(i) + "," + str(loc))
