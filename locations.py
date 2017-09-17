from datetime import datetime, timedelta
class Location(object):
    place = "null"
    date = "0000-00-00"
    depTime = "null"
    
    def __init__(self, place, date):
        self.place = place
        self.date = date
            
    def setDate(self, dur):
        startDate = self.date
        date = datetime.strptime(startDate, "%Y-%m-%d")
        modified_date = date + timedelta(days=dur)
        self.date = datetime.strftime(modified_date, "%Y-%m-%d")
        

