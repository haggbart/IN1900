class Line(object):
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2
    def value(self, x):
        x0, y0 = self.p1[0], self.p1[1]
        x1, y1 = self.p2[0], self.p2[1]
        a = (y1 - y0)/float(x1 - x0)
        b = y0 - a*x0
        return a*x+b

def test_Line():
    line = Line((0,0), (10,10))
    computed = line.value(5)
    expected = 5
    tol = 1e-14
    success = abs(computed - expected) < tol
    msg = 'test line error'
    assert success, msg

# from Line import Line, test_Line
#line = Line((0,-1), (2,4))
#print(line.value(0.5), line.value(0), line.value(1))
#test_Line()


'''
Fra Python Console:

from Line import Line, test_Line
line = Line((0,-1), (2,4))
print(line.value(0.5), line.value(0), line.value(1))
0.25 -1.0 1.5
test_Line()
'''