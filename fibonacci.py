#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:54:09 2018

@author: leo
"""
a,b=0,1
while b<10:
    print(b)
    tmp=a
    a=b
    b=b+tmp
a, b = 0, 1
while b < 10:
     print(b)
     a, b = b, a+b