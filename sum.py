"""
Date: 4/11/2018

@author: Kaleb Robert McKone
"""
import sys

def summation(term, a, compute_next, b):
    if a > b:
        return 0
    else:
        return term(a) + summation(term, compute_next(a), compute_next, b)

def identity(x):
    return x
    
def increment(x):
    x+=1
    return x

def cube(x):
    return x * x * x

def sum_a_to_b_integers(a, b):
    return summation(identity, a, increment, b)

def integral_by_simpsons_rule(f, a, b, n):
    def compute_h():
        if n % 2 != 0:
            print("Error, n is not even.")
            sys.exit(1)
        else:
            return ((b - a) / n)
    def compute_y_sub_k(k):
        if k == n or k == 0:
            return f(a + (k*compute_h()))
        elif k % 2 == 0:
            return 2 * f(a + (k*compute_h()))
        else:
            return 4 * f(a + (k*compute_h()))
    return (compute_h()/3) * summation(compute_y_sub_k, 0, increment, n)


def sum_iter(term, a, compute_next, b):
    def iteration(a, result):
        if a > b:
            return result
        else: 
            return iteration(compute_next(a), result + term(a))
    return iteration(a, 0)

z = sum_iter(identity, 1, increment, 10)
print(z)
        
        
