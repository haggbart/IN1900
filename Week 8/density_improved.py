

def substance(fil):
    infile = open(file, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        key = " ".join(words[:-1])
        density = float(words[-1])
        densities[key] = density
    infile.close()
    return densities


def substance2(file):
    infile = open(file, 'r')
    densities = {}
    d = 12
    for line in infile:
        key =  line[:d].strip()
        density = line[d:].strip()
        densities[key] = float(density)
    infile.close()
    return densities


def test_substance():
    expected = substance(file)
    computed = substance2(file)
    success = (expected == computed)
    msg = 'Test unsuccessful'
    assert success, msg


file = 'densities.dat'
test_substance()


'''
Terminal> density_improved.py"

Process finished with exit code 0
'''