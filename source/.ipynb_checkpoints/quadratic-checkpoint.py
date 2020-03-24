import math

def quadratic_normal(a,b,c):
    if a != 0:
        delta = b*b-4*a*c
        if delta>=0:
            x1 = (-b+math.sqrt(delta))/(2*a)
            x2 = (-b-math.sqrt(delta))/(2*a)
            return [x1,x2]
        else:
            print('The equation has no solution!')
    else:
        if b!=0:
            x = (-c)/b
        else:
            print('Func error!')
            
def quadratic_revert_viete(S,P):
    return quadratic_normal(1,-S,P)