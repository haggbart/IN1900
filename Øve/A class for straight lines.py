class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1
    def __call__(self, x):
        return self.c0 + self.c1*x
    def table(self, L, R, n):
        s = ''
        for x in linspace(L,R,n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

