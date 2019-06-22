#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:32:36 2019
Hackerrank challenge: you are given two complex numbers, and you have to 
print the result of their addition, subtraction, multiplication, 
division and modulus operations.

The real and imaginary precision part should be correct up to two 
decimal places.
    
@author: Leo
"""
from math import sqrt

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        return Complex(self.real+no.real,
                       self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real,
                       self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real -self.imaginary*no.imaginary,
                       self.real*no.imaginary+self.imaginary*no.real)
    def __truediv__(self, no):
        if no.mod().real ==0:
            print('Trying to divide by zero')
            return None
        else:
            return self.__mul__(
                    Complex(no.real, -1*no.imaginary).__mul__(
                            Complex(1.0/(no.mod().real)**2, 0)))
    def mod(self):
        return Complex(sqrt(self.real**2 +self.imaginary**2),0)
    
    def __str__(self):
        if self.imaginary == 0:
            result = '{:.2f}+0.00i'.format(self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = '0.00+{:.2f}'.format(self.imaginary)
            else:
                result = '0.00+{:.2f}'.format((abs(self.imaginary)))
        elif self.imaginary > 0:
            result = '{:.2f}+{:.2f}'.format(self.real, self.imaginary)
        else:
            result = '{:.2f}-{:.2f}'.format(self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())#map object can be converted to list
    d = map(float, input().split())#list(c) for a more convenient form
    x = Complex(*c)#the * unpacks the elements in the iterable c
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')