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


async def update_loc_with_lat_long(loc):
    async with aiohttp.ClientSession() as session:

        para = {
            'access_key': YOUR_ACCESS_KEY,
            'query': loc.address,
            'fields': 'results.latitude',
            'limit': 1,
        }
        url = "http://api.positionstack.com/v1/forward"
        async with session.get(url, params=para) as resp:
            if resp.status == 200:
                b = await resp.json()
                loc.add_long_lat(b)
            else:
                raise


async def update_list_async(locs):
    await asyncio.gather(*[update_loc_with_lat_long(loc) for loc in locs])


def write_to_csv(filename, locs):
    with open(filename, "w") as csv_file:
        csv_file.write("Sortnumber,Distance,Name,Address\n")
        csv_file.write("\n".join([str(i + 1) + "," + str(loc) for i, loc in enumerate(locs)]))


if __name__ == "__main__":
    from datetime import datetime

    start = datetime.now()

    ADDRESS_FILE = "addresses.txt"
    YOUR_ACCESS_KEY = ""
    CSV_FILE = "sorted_distance.csv"
    START = "Adchieve HQ"

    locs = locations.create_location_list(ADDRESS_FILE)
    asyncio.run(update_list_async(locs))
    source = None
    for i, loc in enumerate(locs):
        if loc.name == START:
            source = locs.pop(i)
            break

    for loc in locs:
        loc.distance_from_source(source)

    locs.sort(key=attrgetter('distance'))
    write_to_csv(CSV_FILE, locs)
    end = datetime.now()
    print(end - start)
