constants = {}
infile = open('physics_constants.dat', 'r')
for line in infile:
    words = line.split(':')
    constant = words[1].split()[0]
    name = words[0]
    value = float(words[1].split()[1])
    unit = words[1].split()[2].strip('[]')
    constants[constant] = {'name': name, 'value': value, 'unit': unit}


ke = constants['ke']['value']
me = constants['me']['value']
hbar = constants['hbar']['value']
e = constants['e']['value']


E = (ke**2 * me * e**4) / (2*hbar**2)
print(round(E,20), 'J')


'''
Terminal> constants_hydrogen.py"
2.18e-18 J

Process finished with exit code 0
'''