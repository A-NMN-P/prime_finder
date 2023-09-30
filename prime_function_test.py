# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:34:39 2023

@author: Ahmed Numan Pervane
"""

from prime_finder import Prime_Finder, isPrime

# Find the prime numbers in a specific range:
p, unp, div = Prime_Finder(initilizer = 4, limit = 10, prime_list=True, unprime_list=True, division_list=True, step = 3)

print("\nPrime Numbers: \n", p)
print("\nNone Prime Numbers: \n", unp)
print("\Dividers:\n", div)

# Check the number is prime or not:
primeness, division_list = isPrime(10,True)
print("\nGiven number is prime or not: ", primeness)
print("\nThe division list: ", division_list)

