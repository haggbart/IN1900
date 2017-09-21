# 2.2 (f2c_approx_table.py, side 82)


print('------------------') # table heading
#C = -20                     # start value for C
F = 0
#dC = 5                      #  increment of C in loop
dF = 10
while F <= 100:              # loop heading with condition
    #F = (9.0/5)*C + 32      # 1st statement inside loop
    C = F*5/9-32*5/9
    aC = (F-30)/2
    print("F: %8.2f C: %8.2f C(Approx): %8.2f" % (F, C, aC))             # 2nd statement inside loop
    F += dF                 # 3rd statement inside loop
print('------------------') # end of table line (after loop)


"""
Terminal> f2c_approx_table.py"
------------------
F:     0.00 C:   -17.78 C(Approx):   -15.00
F:    10.00 C:   -12.22 C(Approx):   -10.00
F:    20.00 C:    -6.67 C(Approx):    -5.00
F:    30.00 C:    -1.11 C(Approx):     0.00
F:    40.00 C:     4.44 C(Approx):     5.00
F:    50.00 C:    10.00 C(Approx):    10.00
F:    60.00 C:    15.56 C(Approx):    15.00
F:    70.00 C:    21.11 C(Approx):    20.00
F:    80.00 C:    26.67 C(Approx):    25.00
F:    90.00 C:    32.22 C(Approx):    30.00
F:   100.00 C:    37.78 C(Approx):    35.00
------------------
"""