How to Run:
1. pip install requirements.txt
2. update .env with api key
3. run main.py
4. Further scope: change value of START in .env to calculate distances from other addresses

Workflow:
1. Read addresses from text file and create list of location objects
2. Query geolocation API for longitude latitude of each address asynchronously
3. Update objects in location list with their longitude latitudes
4. Pop the start address from the list
5. Update the distances dict of start_location_obj

distances = {location_obj: distance from self,}

6. Use haversine function to calculate distance using long lat
7. Sort start_location_obj.distances by value
8. Print sorted list of tuples in csv.
