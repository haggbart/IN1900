from math import sqrt


class Rectangle(object):
    def __init__(self, W, H, x0, y0):
        self.W, self.H, self.x0, self.y0 = W, H, x0, y0

    def area(self):
        return self.W * self.H

    def perimeter(self):
        return self.W*2 + self.H*2

def test_Rectangle():
    r = Rectangle(5, 5, 2, -1)
    computed1, computed2 = r.area(), r.perimeter()
    expected1, expected2 = 5*5, 5*2+5*2
    tol = 1e-14
    success1 = abs(computed1 - expected1) < tol
    success2 = abs(computed2 - expected2) < tol
    success = success1 and success2
    msg = 'Rectangle test error'
    assert success, msg
test_Rectangle()


class Triangle(object):
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.v0, self.v1, self.v2 = [x0,y0], [x1,y1], [x2,y2]
        self.vertices = [self.v0, self.v1, self.v2]

    def area(self):
        x1, y1 = self.v0
        x2, y2 = self.v1
        x3, y3 = self.v2
        return 1/2 * abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)

    def perimeter(self):
        s = 0
        for i in range(len(self.vertices)):
            x = (self.vertices[i][0] - self.vertices[i-1][0])
            y = (self.vertices[i][1] - self.vertices[i-1][1])
            s += sqrt(x**2 + y**2)
        return s

def test_Triangle():
    t = Triangle(0,0, 5,5, 10,0)
    computed1, computed2 = t.area(), t.perimeter()
    expected1, expected2 = 1/2 * 10*5, sqrt(5**2+5**2)*2+10
    tol = 1e-14
    success1 = abs(computed1 - expected1) < tol
    success2 = abs(computed2 - expected2) < tol
    success = success1 and success2
    msg = 'Triangle test error'
    assert success, msg
test_Triangle()


r = Rectangle(2, 3, 1, 0)
t = Triangle(0,0, 2,2, 5,0)


print('Area of Rectangle: %g' % r.area())
print('Perimeter: %g' %r.perimeter())
print('lower left corner: (%g, %g)' % (r.x0, r.y0))
print('----------------------------')
print('Area of Triangle: %g' %t.area())
print('Perimeter: %g' % t.perimeter())


'''
Terminal> geometric_shapes.py
Area of Rectangle: 6
Perimeter: 10
lower left corner: (1, 0)
----------------------------
Area of Triangle: 5
Perimeter: 11.434

Process finished with exit code 0
'''