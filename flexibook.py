import requests
import json
import flights
import locations
# requires python requests - to install -> pip install requests
APIKEY = "GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN"

# given origin and destination location objects -> returns array of flights
def getFlights(origin, destination):
    link = 'http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN&origin='+ str(origin.place) +'&destination=' + str(destination.place) +'&departure_date='+ str(origin.date) + '&number_of_results=250&HTTP/1.1'
    r = requests.get(link)
    f = flights.Flights(r.text,0)
    
    print("origin: " + str(f.origin) + ", destination: " + str(f.destination) + ", departs_at: " + str(f.departs_at) + ", arrives_at: " + str(f.arrives_at) + ", airline: " + str(f.airline) + ", price: " + str(f.price) + ", stops: " + str(f.stops))
    return r
# return array with cheapest flights on the selected dates to the selected places
def getMultipleDestinationFlights(origin, destinations):
    flightArray = []
    orig = origin
    for d in destinations:
        f = getFlights(orig,d)
        flightArray.append(flights.Flights(f.text,0))
        orig = d
    return flightArray

#getFlights(locations.Location("BOS",'2017-09-17'), locations.Location("SEA",'0000-00-00'))
dest = []
dest.append(locations.Location("SFO",'2017-09-22'))
dest.append(locations.Location("SEA",'2017-10-04'))
a = getMultipleDestinationFlights(locations.Location("BOS",'2017-09-17'),dest)
print()
print()
print()
for f in a:
    print(f)
    print("---------------" + "origin: " + str(f.origin) + ", destination: " + str(f.destination) + ", departs_at: " + str(f.departs_at) + ", arrives_at: " + str(f.arrives_at) + ", airline: " + str(f.airline) + ", price: " + str(f.price) + ", stops: " + str(f.stops))