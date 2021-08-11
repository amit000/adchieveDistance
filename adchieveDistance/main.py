# read addresses-----done
# bulk query only for longitude lattitude----can't do bulk query in free tier
# query one by one---done
# add long lat to obj--done
# design function to calculate distance using long lat---done
# find out source long latt--done
# find out distance between source and every other address obj,---done
# sort list by distance---done
# print in format---done

import aiohttp
import asyncio
from operator import attrgetter

import locations

locs = locations.create_location_list("addresses.txt")

YOUR_ACCESS_KEY = ""


async def update_loc_with_lat_long(loc):
    async with aiohttp.ClientSession() as session:
        print(f"started for {loc.name}")
        para = {
            'access_key': YOUR_ACCESS_KEY,
            'query': loc.address,
            'fields': 'results.latitude',
            'limit': 1,
        }
        url = "http://api.positionstack.com/v1/forward"
        async with session.get(url, params=para) as resp:
            b = await resp.json()
            loc.add_long_lat(b)


async def update_list_async():
    await asyncio.gather(*[update_loc_with_lat_long(loc) for loc in locs])


asyncio.run(update_list_async())

source = None
for i, loc in enumerate(locs):
    if loc.name == "Adchieve HQ":
        source = locs.pop(i)
        break

for loc in locs:
    loc.distance_from_source(source)

locs.sort(key=attrgetter('distance'))

with open("abc.csv", "w") as csv_file:
    csv_file.write("Sortnumber,Distance,Name,Address\n")
    csv_file.write("\n".join([str(i+1) + "," + str(loc) for i, loc in enumerate(locs)]))



