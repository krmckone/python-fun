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

# An abstraction of procedures for computing sums or products
def accumulate_linear_recursion(combiner, null_value, term, a, compute_next, b):
    if a > b:
        return null_value
    else:
        return combiner(term(a), 
                        accumulate_linear_recursion(combiner, 
                                   null_value, 
                                   term, 
                                   compute_next(a), 
                                   compute_next, 
                                   b
                        )
                )

def accumulate_iterative_recursion(combiner, null_value, term, a, compute_next, b):
    def accumulate_iter(a, result):
        if a > b:
            return result
        else:
            return accumulate_iter(compute_next(a), combiner(a, result))
    return accumulate_iter(a, null_value)


def sum_with_accumulate(term, a, compute_next, b):
    def sum_values(x,y):
        return x + y
    return accumulate_linear_recursion(sum_values, 0, identity, a, increment, b)

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
