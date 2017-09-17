import json
class Flights(object):

    origin = "null"
    destination = "null"
    departs_at = "0000-00-00T00:00"
    arrives_at = "0000-00-00T00:00"
    price = "0.0"
    airline = "null"
    stops = 0

    def __init__(self, jsonflightinfo, flight_index):
        flight_data = json.loads(jsonflightinfo)
        outbound_flight = flight_data["results"][flight_index]["itineraries"][0]["outbound"]["flights"][0]
        lastFlight = flight_data["results"][flight_index]["itineraries"][0]["outbound"]["flights"][-1]
        self.origin = outbound_flight["origin"]["airport"]
        self.destination = lastFlight["destination"]["airport"]
        self.departs_at = outbound_flight["departs_at"]
        self.arrives_at = lastFlight["arrives_at"]
        self.airline = outbound_flight["marketing_airline"]
        self.price = flight_data["results"][flight_index]["fare"]["total_price"]
        self.stops = len(flight_data["results"][flight_index]["itineraries"][0]["outbound"]["flights"]) - 1




