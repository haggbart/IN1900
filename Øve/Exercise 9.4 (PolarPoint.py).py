from math import cos, sin, pi


class Point:
    def __init__(self, x,y):
        self.x, self.y = x,y
    def __str__(self):
        return '(%g, %g)'% (self.x, self.y)



class PolarPoint(Point):
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta
        x = r*cos(theta)
        y = r*sin(theta)
        Point.__init__(self,x,y)

    def __str__(self):
        return '(r, theta) = (%g, %g), (x, y) = (%g, %g)'\
               % (self.r, self.theta, self.x, self.y)


origo = PolarPoint(0,pi)
p1 = PolarPoint(1,pi/2)
print(origo)
print(p1)