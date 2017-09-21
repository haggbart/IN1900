# 2.5 (sum_int.py, side 82)

"""
Write a program that computes the sum of the integers from 1 up to and including
n. Compare the result with the famous formula n(n+1)/2.
Filename: sum_int.
"""
sum = 0
n = 10
for i in range(1,n+1):
    sum += i
print(sum)