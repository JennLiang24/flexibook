import flexibook
import itertools

#generates all possible permutations of the middle locations
def generatePermutations(list_of_locations):
    #eliminate last location because should be the same as origin
    list_to_permutate = list_of_locations[:-1]

    loc_permutations = list(itertools.permutations(list_to_permutate, len(list_to_permutate)))
    print(loc_permutations)
    return loc_permutations


#finds the cheapest order
def findCheapestOrder(origin, list_of_locations):
    list_of_orders = generatePermutations(list_of_locations)
    price =
    for i in list_of_orders:
        flexibook.getMultipleDestinationFlights(origin, i).price


generatePermutations(["BOS", "NYC", "LAX", "SEA"])
