# Exercise 4.2
# We know that F = (9/5)C + 32, so C = (5/9)(F-32)
import sys
F = float(sys.argv[1])


#F = float(input("Temp in Fahrenheit = ? "))
C = (5.0/9)*(F-32)
print("Tempe in Celsius: %g" % C)


