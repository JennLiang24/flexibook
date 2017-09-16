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
        outbound_flight_index = flight_data["results"][flight_index][0]["itineraries"][0]["outbound"]["flights"][0]
        outbound_fare_index = flight_data["results"][flight_index][1]["fare"]
        origin = outbound_flight_index["origin"]["airport"]
        destination = outbound_flight_index[1]["destination"]["airport"]
        departs_at = outbound_flight_index[0]["origin"]["departs_at"]
        arrives_at = outbound_flight_index[0]["origin"]["arrives_at"]
        airline = outbound_flight_index[0]["origin"]["airport"]
        price = outbound_fare_index["total_price"]



