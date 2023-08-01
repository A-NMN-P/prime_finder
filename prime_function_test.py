# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:34:39 2023

@author: Ahmed Numan Pervane
"""

from prime_finder import Prime_Finder, isPrime

p, unp, div = Prime_Finder(initilizer = 4, limit = 10, prime_list=True, unprime_list=True, division_list=True, step = 3)

print("\nAsal sayılar: \n", p)
print("\nAsal olmayan sayılar: \n", unp)
print("\nBölenler:\n", div)


