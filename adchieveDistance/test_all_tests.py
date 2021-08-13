import unittest
import haversine
import locations
import main


class TestAll(unittest.TestCase):
    def test_haversine(self):
        lat1 = 51.5007
        lon1 = 0.1246
        lat2 = 40.6892
        lon2 = 74.0445

        self.assertEqual(haversine.haversine(lat1, lon1, lat2, lon2), 5574.840456848555)

    def test_find_distance_geodata(self):
        a = locations.Location("a", "addadd")
        b = locations.Location("b", "addadd")
        a.latitude = 51.5007
        a.longitude = 0.1246
        b.latitude = 40.6892
        b.longitude = 74.0445
        self.assertEqual(haversine.find_distance_geodata(a, b), 5574.840456848555)

    def test_add_long_lat(self):
        a = locations.Location("a", "addr")
        a.add_long_lat({'data': [{'latitude': 52.26633, 'longitude': 6.78576}]})
        self.assertEqual(a.latitude, 52.26633)
        self.assertEqual(a.longitude, 6.78576)

    def test_distance_from_self(self):
        a = locations.Location("a", "addadd")
        b = locations.Location("b", "addadd")
        a.latitude = 51.5007
        a.longitude = 0.1246
        b.latitude = 40.6892
        b.longitude = 74.0445
        a.distance_from_self([b])
        self.assertEqual(a.distance[b], 5574.840456848555)
