import requests
import json
import flights
import datetime

# requires python requests - to install -> pip install requests
APIKEY = "GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN"

#stores the index of the flight option
flight_index = 0

# given origin and destination location objects -> returns array of flights
def getFlights(origin, destination):
    r = requests.get('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN&origin=BOS&destination=SEA&departure_date=2017-09-17&number_of_results=100&HTTP/1.1', APIKEY)
    fly = flights.Flights(r.text,flight_index)
    return fly

#takes the current flight index and current Location originlocation and
#finds next possible flight to arrive at the destination earlier
def flightEarlier(flight_index, originlocation):
    r = requests.get('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=QQ6BE8Rvtf5MEGv8bnj3wIgA7FjYljja&origin=BOS&destination=LON&departure_date=2017-12-25&number_of_results=100 HTTP/1.1')
    fly = flights.Flights (r.text, flight_index)
    flight_data = json.loads(r.text)

    #the number of flight results
    length_results = len(flight_data["results"])
    length_results = 20


    for i in range(flight_index, length_results):
        fly2 = flights.Flights(r.text, i)

        # converts string time to datetime format
        arrivaloriginal = datetime.datetime.strptime(fly.arrives_at,'%Y-%m-%dT%H:%S')
        arrivalnew = datetime.datetime.strptime(fly2.arrives_at,'%Y-%m-%dT%H:%S')

        if(arrivaloriginal > arrivalnew):
            print("The earlier flight time is " + fly2.arrives_at)
            fly = fly2
            flight_index = 0
            return fly

    print("No earlier flights found")
    return

#takes the current flight index and current Location originlocation and
#finds next possible flight to depart later
def flightLater(flight_index, originlocation):
    r = requests.get('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=QQ6BE8Rvtf5MEGv8bnj3wIgA7FjYljja&origin=BOS&destination=LON&departure_date=2017-12-25&number_of_results=100 HTTP/1.1')
    fly = flights.Flights (r.text, flight_index)
    flight_data = json.loads(r.text)

    #the number of flight results
    length_results = len(flight_data["results"])

    for i in range(flight_index, length_results):
        fly2 = flights.Flights(r.text, i)

        # converts string time to datetime format
        departureoriginal = datetime.datetime.strptime(fly.departs_at,'%Y-%m-%dT%H:%S')
        departurenew = datetime.datetime.strptime(fly2.departs_at,'%Y-%m-%dT%H:%S')

        if(departureoriginal < departurenew):
            print("The later flight time is " + fly2.departs_at)
            fly = fly2
            flight_index = 0
            return fly

    print("No later flights found")
    return

getFlights("dfbhj", "aejhf")

flightLater(0,0)

    