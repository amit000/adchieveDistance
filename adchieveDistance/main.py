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
from datetime import datetime
from dotenv import load_dotenv
import locations
import os


async def update_loc_with_lat_long(loc):
    async with aiohttp.ClientSession() as session:

        para = {
            'access_key': os.getenv('ACCESS_KEY'),
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
                print("invalid response")


async def update_list_async(locs):
    await asyncio.gather(*[update_loc_with_lat_long(loc) for loc in locs])


def write_to_csv(filename, distances):
    with open(filename, "w") as csv_file:
        csv_file.write("Sortnumber,Distance,Name,Address\n")
        row = 1
        for location, dist in distances:
            csv_file.write(str(row) + "," + str(f"{dist:.2f} km,") + str(location) + "\n")
            row += 1


if __name__ == "__main__":

    load_dotenv()

    start = datetime.now()
    locs = locations.create_location_list(os.getenv('ADDRESS_FILE'))
    asyncio.run(update_list_async(locs))

    START = "Adchieve HQ"

    source = None
    for i, loc in enumerate(locs):
        if loc.name == START:
            source = locs.pop(i)
            break

    source.distance_from_self(locs)

    sort_distances = sorted(source.distance.items(), key=lambda x: x[1])
    write_to_csv(os.getenv('CSV_FILE'), sort_distances)
    end = datetime.now()
    print(end - start)
