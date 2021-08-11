import haversine


class Location:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.longitude = None
        self.latitude = None
        self.distance = None

    def __repr__(self):
        if not self.distance:
            return self.name + self.address
        else:
            return "\",\"".join(['"'+f"{self.distance:.2f}"+" km", self.name , self.address+'"'])

    def add_long_lat(self, data):
        try:
            self.longitude = data["data"][0]["longitude"]
            self.latitude = data["data"][0]["latitude"]
        except Exception as e:
            print("invalid response")

    def distance_from_source(self, source):
        if self.longitude and self.latitude and source.longitude and source.latitude:
            self.distance = haversine.find_distance_geodata(self, source)
        else :
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
