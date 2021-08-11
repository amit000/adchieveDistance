import haversine


class Location:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.longitude = None
        self.latitude = None
        self.distance = {}

    def __repr__(self):
        if not self.distance:
            return "\"" + self.name + "\",\"" + self.address + "\""

    def add_long_lat(self, data):
        try:
            self.longitude = data["data"][0]["longitude"]
            self.latitude = data["data"][0]["latitude"]
        except Exception as e:
            print("invalid response")

    def distance_from_self(self, targets):
        if self.longitude and self.latitude:
            for target in targets:
                if target.longitude and target.latitude:
                    self.distance[target] = haversine.find_distance_geodata(self, target)
        else:
            print("invalid latitude longitudes")


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
