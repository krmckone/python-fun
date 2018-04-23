import math

def cons(a,b):
    return lambda m: m((2**a)*(3**b),a,b)

def car(z):
    return z(lambda total, a, b: math.log((total/3**b),2))

def cdr(z):
    return z(lambda total, a, b: math.log((total/2**a),3))

print(car(cons(1,2)))
print(cdr(cons(1,2)))