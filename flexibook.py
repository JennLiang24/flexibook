import requests
import json
import flights
# requires python requests - to install -> pip install requests
APIKEY = "GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN"

# given origin and destination location objects -> returns array of flights
def getFlights(origin, destination):
    r = requests.get('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN&origin=BOS&destination=SEA&departure_date=2017-09-17&number_of_results=2&HTTP/1.1')
    fly = flights.Flights(r.text,0)
    
    print(r.text)
    
    
getFlights("dfbhj", "aejhf")

    