# read addresses
# bulk query only for longitude lattitude
# design function to calculate distance using long lat
# find out source long latt
# find out distance between source and every other address, add distance to the obj/dict
# sort objs/dicts by distance
# print in format

# Python 3
import http.client, urllib.parse

conn = http.client.HTTPConnection('api.positionstack.com')

YOUR_ACCESS_KEY = "abc123"

params = urllib.parse.urlencode({
    'access_key': YOUR_ACCESS_KEY,
    'query': 'Eastern Enterprise - 46/1 Office no 1 Ground Floor , Dada House , Inside dada silk mills compound, Udhana Main Rd, near Chhaydo Hospital, Surat, 394210, India',

    })

conn.request('GET', '/v1/forward?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))