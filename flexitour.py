import flexibook
import sys
import itertools
import locations
import flights
import userinput


#generates all possible permutations of the middle locations
def generatePermutations(list_of_locations):
    #eliminate last location because should be the same as origin
    list_to_permutate = list_of_locations[:-1]

    loc_permutations = list(itertools.permutations(list_to_permutate, len(list_to_permutate)))
    return loc_permutations


#finds the cheapest order and returns it as an array
def findCheapestOrder(origin, list_of_locations):
    list_of_orders = generatePermutations(list_of_locations)
    minprice = sys.float_info.max
    minorder = []
    for i in list_of_orders:

        destinations = list(i) + [origin]
        originloc = locations.Location(origin[0], userinput.origin_date)
        daysfromorigin = 0
        destinationlocs = []
        for j in destinations:
            destinationlocs += [locations.Location(destinations[0], userinput.origin_date)]
            daysfromorigin += destinations[1] + 1
            destinationlocs[j].locations.setDate(daysfromorigin)

        flight_itinerary = flexibook.getMultipleDestinationFlights(originloc, destinationlocs)

        if flight_itinerary.price < minprice:
            minorder = flight_itinerary
            minprice = flight_itinerary.price

    return minorder

