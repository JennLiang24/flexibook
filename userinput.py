
#initialize origin date to be modified in setOriginDepDate()
origin_date = "0000-00-00"

#initialize origin location to be modified in
originlocation = "NUL"

#initialize destinations and durations to be put into flexitour.generatePermutations() and
#modified in setLocations()
list_of_locs = []


#sets origin_date
def setOriginDate(userinput):
    global origin_date
    origin_date = userinput

#sets originlocation
def setOriginLocation(userinput):
    global originlocation
    originlocation = userinput

#user input for destination and duration should be stored with first input as origin tuple
#and all other inputs as tuples (location, duration)
# elements in an array to be used as inputs for findCheapestOrder()
def setLocations(userinputloc, userinputdur):
    global list_of_locs
    list_of_locs = list_of_locs + [(userinputloc, userinputdur)]

