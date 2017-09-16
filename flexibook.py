import requests
import json
# requires python requests - to install -> pip install requests
APIKEY = "GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN"

# given origin and destination location objects -> returns array of flights
def getFlights(origin, destination):
    r = requests.get('http://api.sandbox.amadeus.com/v1.2/flights/extensive-search?apikey=GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN&origin=FRA&destination=LON&departure_date=2017-09-17&one-way=true&HTTP/1.1')
    
    
    print(r.text)
    
    
getFlights("dfbhj", "aejhf")

    