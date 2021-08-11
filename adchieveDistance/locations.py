import haversine

class Location:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __repr__(self):
        return self.name + self.address

    def add_long_lat(self,data):
        self.longitude = data.longitude
        self.latitude = data.latitude

    def distance_from_source(self,source):
        self.distance = find_distance_geodata(self,source)




def create_location_list(filename):
    locations = []
    with open(filename) as addresses:
        lines = addresses.readlines()
        for line in lines:
            if line:
                name, address = line.split("-", 1)

                locations.append(Location(name.strip(), address.strip()))
    return locations


if __name__ == "__main__":
    locations = create_location_list("addresses.txt")
    print(locations)
