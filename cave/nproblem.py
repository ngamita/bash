# -*- coding: utf-8 -*-
"""
Problem: Given input N, print cubes of first N natural numbers.
Also make sure that N is less than or equal to 100. 

Created on Tue Sep 20 22:04:14 2016

@author: ngamita
"""
n = 0
while(n <= 100):
    for num in range(0,n):
        print(num**3)
    n = int(raw_input('Enter n: '))
        #n+=1
        #print(n**