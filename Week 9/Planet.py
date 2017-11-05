from math import pi
class Planet(object):
    def __init__(self, navn, radius, masse):
        self.n, self.r, self.m = navn, radius, masse
        self.populasjon = 7497486172

    def density(self):
        return self.m / ((4*pi*self.r**3)/3)
    def print_info(self):
        print('Navn: %s' % self.n)
        print('Radius: %g m' % self.r)
        print('Masse: %g kg' % self.m)
        print('Massetetthet: %g kg/m^3' % self.density())
        print('Populasjon: %g' % self.populasjon)


planet1 = Planet('Jorden', 6371e3, 5.972e24)
planet1.print_info()
print('-----------------------------')
print(planet1.n, "har en populasjon på ", planet1.populasjon)


'''
Terminal> Planet.py"
Navn: Jorden
Radius: 6.371e+06 m
Masse: 5.972e+24 kg
Massetetthet: 5513.26 kg/m^3
Populasjon: 7.49749e+09
-----------------------------
Jorden har en populasjon på  7497486172

Process finished with exit code 0
'''