# -*- coding: utf-8 -*-
# 给一个数字在range [0, 1million]  找出来到最近的Fibnacci数字的距离
# Test examples:
#Fibonacci range wrapping 1044 is [987, 1597]
#Fibonacci range wrapping 8999913 is [5702887, 9227465]
#Fibonacci range wrapping 7 is [5, 8]
#Fibonacci range wrapping 67 is [55, 89]

# Recurson is too slow!!!
#def F(n):
#    if n == 0: return 0
#    elif n == 1: return 1
#    else: return F(n-1)+F(n-2)

phi = (1 + 5**0.5) / 2

# Because of floating-point rounding errors, this formula will only give the right result for n < 70.
def F(n):
    return int(round((phi**n - (1-phi)**n) / 5**0.5))

from math import log    
def FindStep(n):
    if n <= 1: return 1-n
    else:
        # Use the inverse Fibonacci function to find a rough estimate, 
        # see: https://en.wikipedia.org/wiki/Fibonacci_number#Relation_to_the_golden_ratio
        # http://stackoverflow.com/questions/7843048/finding-the-closest-fibonacci-numbers?rq=1
        i = int(round(log(n * 5**0.5) / log(phi)))  
        
        if F(i)<n:
            #print F(i), F(i+1)
            return min(abs(n-F(i)),abs(F(i+1)-n))
        else:
            #print F(i-1), F(i)
            return min(abs(n-F(i-1)),abs(F(i)-n))