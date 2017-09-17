import json
class Flights(object):

    origin = "null"
    destination = "null"
    departs_at = "0000-00-00T00:00"
    arrives_at = "0000-00-00T00:00"
    price = "0.0"
    airline = "null"

    def __init__(self, jsonflightinfo, flight_index):
        flight_data = json.loads(jsonflightinfo)
        outbound_flight_index = flight_data["results"][flight_index]["itineraries"][0]["outbound"]["flights"][0]
        self.origin = outbound_flight_index["origin"]["airport"]
        self.destination = outbound_flight_index["destination"]["airport"]
        self.departs_at = outbound_flight_index["departs_at"]
        self.arrives_at = outbound_flight_index["arrives_at"]
        self.airline = outbound_flight_index["operating_airline"]
        self.price = flight_data["results"][flight_index]["fare"]["price_per_adult"]["total_fare"]




