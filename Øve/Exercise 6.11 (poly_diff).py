

def poly_diff(p):
    dp = {}
    for j in p:
        if j != 0:
            dp[j-1] = j*p[j]
    return dp


# = 1 + x + x**2
p = {0:1,1:1,2:1}


#dp = 1 + 2*x
dp_ref = {0:1,1:2}

p2 = {0:-1.5,100:2}

dp = poly_diff(p)
print(dp_ref)
print(dp)
print(poly_diff(p2))

