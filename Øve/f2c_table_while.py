print('------------------') # table heading
#C = -20                     # start value for C
F = 0
#dC = 5                      #  increment of C in loop
dF = 10
while F <= 100:              # loop heading with condition
    #F = (9.0/5)*C + 32      # 1st statement inside loop
    C = F*5/9-32*5/9
    print(F, C)             # 2nd statement inside loop
    F += dF                 # 3rd statement inside loop
print('------------------') # end of table line (after loop)


