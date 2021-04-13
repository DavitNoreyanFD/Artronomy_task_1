class Stars:
    def __init__(self, id, ra, dec, mag, flux, distance=None):
        self.id = id
        self.ra = ra
        self.dec = dec
        self.mag = mag
        self.flux = flux
        self.distance = distance

    def __repr__(self):
        return f'{self.id}, {self.ra}, {self.dec}, {self.mag}, {self.flux}, {self.distance}'
