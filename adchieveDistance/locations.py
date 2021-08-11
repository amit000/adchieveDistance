import haversine


class Location:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __repr__(self):
        if not self.distance:
            return self.name + self.address
        else:
            return "\",\"".join(['"'+f"{self.distance:.2f}"+" km", self.name , self.address+'"'])

    def add_long_lat(self, data):
        self.longitude = data["data"][0]["longitude"]
        self.latitude = data["data"][0]["latitude"]

    def distance_from_source(self, source):
        self.distance = haversine.find_distance_geodata(self, source)


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
