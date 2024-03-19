class NationalPark:

    def __init__(self, name):

            self.name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):

        if hasattr(self, "name"):
            print("You Hecked Up")
        elif type(name) == str and len(name) >= 3:
            self._name = name
        
    name = property(get_name, set_name)
    
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        count = 0
        for trip in Trip.all:
            if trip.national_park == self:
                count += 1
        return count
    
    def best_visitor(self):
        visitor_counter = {}
        for trip in Trip.all :
            if trip.national_park == self:
                if trip.visitor not in visitor_counter:
                    visitor_counter[trip.visitor]=1
                else:
                    visitor_counter[trip.visitor]+=1
        sorted_vis = sorted(visitor_counter.items(), key=lambda key:key[1], reverse=True)
        return sorted_vis[0][0]




class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        if type(visitor) is Visitor:
            self.visitor = visitor
        else:
            raise Exception("expecting visitor object")
        if type(national_park) is NationalPark:
            self.national_park = national_park
        else:
            raise Exception("expecting national park object")

        Trip.all.append(self)

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, start_date):
        if type(start_date) == str and len(start_date) >= 7:
            self._start_date = start_date
        else:
            print("dates must be strings greater than 6 characters")
        
    start_date = property(get_start_date, set_start_date)

    def get_end_date(self):
        return self._end_date
    
    def set_end_date(self, end_date):
        if type(end_date) == str and len(end_date) >= 7:
            self._end_date = end_date
        else:
            print("dates must be strings greater than 6 characters")
    end_date = property(get_end_date, set_end_date)
        

class Visitor:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            print("Must be a string between 1-15 characters")

    name = property(get_name, set_name)
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in Trip.all if trip.visitor == self})
    
    def total_visits_at_park(self, park):
        pass