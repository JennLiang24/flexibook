import requests
import json
import flights
import locations
import datetime
import flexitour
import userinput

# requires python requests - to install -> pip install requests
APIKEY = "GP0KwjT7Gkv5ea6wCWuIwonyUKZOVBKN"

#stores the index of the flight option
flight_index = 0
totalPriceOfLastTripCalculated = 0


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
    totalPrice = 0
    orig = origin
    for d in destinations:
        f = getFlights(orig,d)
        fly = flights.Flights(f.text,0)
        totalPrice += fly.price
        flightArray.append(fly)
        orig = d
    totalPriceOfLastTripCalculated = totalPrice
    return flightArray

    #getFlights(locations.Location("BOS",'2017-09-17'), locations.Location("SEA",'0000-00-00'))
dest = []
dest.append(locations.Location("SFO",'2017-09-22'))
dest.append(locations.Location("SEA",'2017-09-28'))
dest[0].setDate(2)
a = getMultipleDestinationFlights(locations.Location("BOS",'2017-09-17'),dest)
#print()
#print()
#print()
#for f in a:
    #print(f)
    #print("---------------" + "origin: " + str(f.origin) + ", destination: " + str(f.destination) + ", departs_at: " + str(f.departs_at) + ", arrives_at: " + str(f.arrives_at) + ", airline: " + str(f.airline) + ", price: " + str(f.price) + ", stops: " + str(f.stops))


#takes the current flight index and current Location originlocation and
#finds next possible flight to arrive at the destination earlier
def flightEarlier(flight_index, originlocation):
    r = requests.get('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=QQ6BE8Rvtf5MEGv8bnj3wIgA7FjYljja&origin=BOS&destination=LON&departure_date=2017-12-25&number_of_results=100 HTTP/1.1')
    fly = flights.Flights (r.text, flight_index)
    flight_data = json.loads(r.text)

    #the number of flight results
    length_results = len(flight_data["results"])

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


#TODO
#create main function that calls setOriginDate() and setOrigin() and setDestinations()


