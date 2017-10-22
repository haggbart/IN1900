# Exercise A.3


x0 = 100
p = 5
r = p/360
import datetime
date1 = datetime.date(2007, 8, 3)
date2 = datetime.date(2011, 8, 3)
diff = date2 - date1
N = diff.days


xnm1 = x0
n = 0
outfile = open('growt_years_efficient.txt', 'w')
while n < (N):
    xn = xnm1 + (r/100)*xnm1
    outfile.write(str(xn) + '\n')
    xnm1 = xn
    n += 1
outfile.close()
print(round(xn,2))


'''
Terminal> growth_years_efficient.py"
122.5

Process finished with exit code 0
'''