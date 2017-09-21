# 2.13 (interest_rate_loop.py, side 85)

"""
a) Use a pocket calculator or an interactive Python shell and work through the
program calculations by hand. Write down the value of amount and years in
each pass of the loop.
b) Set p = 5 instead. Why will the loop now run forever? (Apply Ctrl+c, see Exercise
2.11, to stop a program with a loop that runs forever.) Make the program
robust against such errors.
c) Make use of the operator += wherever possible in the program.
d) Explain with words what type of mathematical problem that is solved by this
program.
"""

initial_amount = 100
p = 5.5 # interest rate
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
    amount = amount + p/100*amount
    years += 1
print(years)

