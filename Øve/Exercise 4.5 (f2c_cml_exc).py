# Exercise 4.2
# We know that F = (9/5)C + 32, so C = (5/9)(F-32)
import sys

try:
    F = float(sys.argv[1])
except IndexError:
    print('Command line argument missing')
    exit()
except ValueError:
    print('Wrong format')
    exit()
#F = 40

#F = float(input("Temp in Fahrenheit = ? "))
C = (5.0/9)*(F-32)
print("Tempe in Celsius: %g" % C)


