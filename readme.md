1. Read addresses from text file and create list of location objects
2. Query geolocation API for longitude latitude of each address asynchronously
3. Update objects in location list with their longitude latitudes
4. Pop the start address from the list
5. Update the distances dict of start_location_obj

distances = {location_obj: distance from self,}

6. Use haversine function to calculate distance using long lat
7. Sort start_location_obj.distances by value
8. Print sorted list of tuples in csv.
