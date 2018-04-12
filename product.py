# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 07:25:19 2018

@author: Kaleb Robert McKone
"""

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

def increment(x):
        x+=1
        return x

def identity(x):
        return x
    
def product_with_accumulate(term, a, compute_next, b):
    def product(a,b):
        return a * b
    return accumulate_linear_recursion(product, 1, term, a, compute_next, b)
    
def product_linear_recursion(term, a, compute_next, b):
    if a > b:
        return 1
    else:
        return term(a) * product_linear_recursion(term, compute_next(a), compute_next, b)

def product_iterative_recursion(term, a, compute_next, b):
    def product_iter(a, result):
        if a > b:
            return result
        else: 
            return product_iter(compute_next(a), result * term(a))
    return product_iter(a, 1)

def factorial_linear_recursion(n):
    return product_linear_recursion(identity, 1, increment, n)

def factorial_iterative_recursion(term, a, compute_next, b):
    return product_iterative_recursion(identity, a, compute_next, b)

def approx_pi_linear_recursion(n): # Wallis Product Approximation of pi/2: https://www.wikiwand.com/en/Wallis_product
    def compute_first_ratio_of(k):
        return (2*k) / (2*k - 1)
    def compute_second_ratio_of(k):
        return (2*k) / (2*k + 1)
    def compute_term(k):
        return compute_first_ratio_of(k) * compute_second_ratio_of(k)
    return product_linear_recursion(compute_term, 1, increment, n)

