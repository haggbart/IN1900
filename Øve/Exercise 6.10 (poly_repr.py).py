

def eval_poly_dict(poly, x):
    sum = 0.0
    for power in poly:
        sum += poly[power]*x**power
    return sum


def eval_poly_list(poly, x):
    sum = 0
    for power in range(len(poly)):
        sum = sum + poly[power]*x**power
    return sum


poly_dict = {0:-0.5,100:2}

poly_list = [0]*101
poly_list[0] = -0.5
poly_list[100] = 2
print(poly_dict)
print(poly_list)

print(eval_poly_dict(poly_dict,1.05))
print(eval_poly_list(poly_list,1.05))