#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:03:37 2018
Creates a csv database listing the parameters used for simulations stored
in a folder hierarchy. Each row of the csv file corresponds to the contents
of an individual input file containing the values of the parameters of a 
particular simulation. Files 'input' and 'simulations.csv' are examples of
the input and output of this function.
@author: Leo
"""
import os

def cleanRows(fname,firstRow):
    """
    Opens the file fname (text) and returns a string, either the first row
    (if firstRow=True) of a csv data file containing the column names,
    or a row with numerical values separated with commas
    """
    rowT=''
    row=''
    file = open(fname,'rt')  #read text file   
    tmp=file.readlines()
    if firstRow:
        for line in tmp:
            value=line.split(sep='!')
            strB=value[1]
            #cleaning strings
            strB=strB.replace('\t','')
            strB=strB.replace('\n','')
            if ',' in strB:
                strB=strB.replace(',','')
            rowT=rowT+strB+','
        return rowT+'\n'
    else:
        for line in tmp:
            value=line.split(sep='!')
            strA=value[0]
            #cleaning strings
            strA=strA.replace('\t','')
            strA=strA.replace('d0','0')  #double precision floats
            strA=strA.replace('d-','e-') #double precision floats
            if '.' in strA:
                row=row+str(float(strA))+','
            else:
                row=row+str(int(strA))+','
        return row+'\n'

csv = input("Desired name for the data file: ") 
dataFile = open(csv,'wt')
rootD= input("name of directory for search: ")
firstR=True
for root, dirs, files in os.walk(rootD): #does an iterative search
    for file in files:
        if file == 'input':
            if firstR:
                csv=cleanRows(os.path.join(root, file),True)
                firstR=False
            csv=csv+cleanRows(os.path.join(root, file),False)

dataFile.write(csv)
dataFile.close()
