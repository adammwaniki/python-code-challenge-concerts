class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value: str):
        # Inserting an extra condition to handle corner cases like the someone declaring the title as None
        if hasattr(self, '_hometown') and self._hometown is not None:
            raise AttributeError("Hometown can only be set once.")
        if isinstance(value, str) and len(value) >= 1:
            self._hometown = value
        else:
            raise ValueError("Hometown must be a non-empty string.")

    def concerts(self):
        pass

    def venues(self):
        pass

    def play_in_venue(self, venue, date):
        pass

    def all_introductions(self):
        pass


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")
        
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise TypeError("Band must be an instance of the type Band")
        
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise TypeError("Venue must be an instance of the type Venue")

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        pass

    def bands(self):
        pass
