import json
class Flights(object):

    origin = "null"
    destination = "null"
    departure_date = "null"
    price = "0.0"
    airline = "null"

    def __init__(self, jsonflightinfo, flight_index):
        flight_data = json.loads(jsonflightinfo)
        origin = flight_data["origin"]
        destination = flight_data["results"][flight_index]["destination"]
        departure_date = flight_data["departure_date"]
        price = flight_data["results"]["price"]
        airline = flight_data["results"][flight_index]["airline"]
        


