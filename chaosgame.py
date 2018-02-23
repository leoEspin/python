#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:06:46 2018
Generate random point P0 (preferably inside triangle a1,b1 -> a3,b3)
    generate random number i, choosing between 1,2,3
    Pnext is point at halfway distance between P0 and ai,bi
    repeat    
@author: leo
"""
import random as rdm
import matplotlib.pyplot as plt
import numpy as np
#for x in range(10):
#  print(rdm.randint(1,3)) #random integer
a1,b1=0,0
a2,b2=1,0
a3,b3=0.5,np.sqrt(1.5)
def nextPoint(current,vertex):
    if vertex == 1:
        return [current[0]+0.5*(a1-current[0]),current[1]+0.5*(b1-current[1])]
    elif vertex==2:
        return [current[0]+0.5*(a2-current[0]),current[1]+0.5*(b2-current[1])]
    else:
        return [current[0]+0.5*(a3-current[0]),current[1]+0.5*(b3-current[1])]


fig, ax = plt.subplots()
ax.plot(a1,b1,'.')
ax.plot(a2,b2,'.')
ax.plot(a3,b3,'.')

p0=rdm.uniform(0,0.5)
q0=rdm.uniform(0,np.sqrt(3)*p0) #inside first-half of triangle
ax.plot(p0,q0,'.')
nextP=[p0,q0]
for i in range(1,5000):
    ind=rdm.randint(1,3)
    nextP=nextPoint(nextP,ind)
    if ind == 1:
        ax.plot(nextP[0],nextP[1],'g.')
    elif ind==2:
        ax.plot(nextP[0],nextP[1],'b.')
    else:
        ax.plot(nextP[0],nextP[1],'r.')   
    
plt.savefig("Sierpinski.pdf")
plt.show()

    


def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]

