from math import *

def comptrap(func,a,b,m):
    h = float((b - a)/m)
    c = float((b + a)/2)
    inner = func(a) + (2 * sum([func((a + (i * h))) for i in range(1,m)])) + func(b)
    err = ((b - a) / 12) * (h ** 2) * (2 * (2 * exp(c ** 2) * (2 * (c ** 2) + 1)))
    full = ((h /2) * inner)
    return(full, 1.46265 - full)

def func(r):
    return(exp(pow(r, 2)))

def simpsons(func, a, b, m):
    h = float((b - a)/ m)
    c = float((b + a)/2)
    sum1 = sum(([4 * func((((i)) * h)) for i in range(1, m + 1, 2)]))
    sum2 = sum([2 * func(a + ((i) * h)) for i in range(2, m , 2)])
    err = 4 * func(c) * ((4 * pow(c,4)) + (12 * pow(c,2)) + 3) #fourth derivative
    rrr = (h/3) * (func(a) + sum1 + sum2 + func(b)) - ((b - a)/180 * (pow(h, 4)) * err)
    return(rrr, 1.46265 - rrr)



