#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:03:37 2018
Creates a csv database listing the parameters used for simulations stored
in a folder hierarchy. Each row of the csv file corresponds to the contents
of an individual input file containing the values of the parameters of a 
particular simulation. Files 'input' and 'simulations.csv' are examples of
the input and output of this code.
@author: Leo
"""
class simulationData:
    paramFile=''
    storeFile=''
    directory=''
    commentSeparator='!' #comment separator in Fortran90
    headerReplaceTup=[(',',''),('\t',''),('\n','')] #must remove commas
    bodyReplaceTup=[('\t',''),('d0','0'),('d-','e-')]#double precision floats
    
    def __init__(self):  
        self.paramFile=(input("Name of input parameter file (defalut \"input\"): ")\
                        or 'input')
        tmp=input("Desired name for the data file: ")
        if tmp.find('.')==-1: #if no file extension given
            tmp=tmp+'.csv'
        self.storeFile=tmp 
        self.directory= input("name of directory for search: ")
        print('\n**Required information about structure of parameter file**:')
        self.commentSeparator=(input("Comment separator (Fortran90 defalut \"!\"): ")\
                               or '!')
        tmp=input('Extra header elements to be replaced '+\
                  'entered as tuples: '+\
                  '\n(currently '+str(self.headerReplaceTup) +')')
        if tmp != '':
            self.headerReplaceTup.append(tmp)
        tmp=input('Extra Body elements to be replaced '+\
                  'entered as tuples: '+\
                  '\n(currently '+str(self.bodyReplaceTup) +')')
        if tmp != '':
            self.bodyReplaceTup.append(tmp)
        #self.fileSearch() #better let the user run this

    def fileSearch(self):
        os = __import__('os')
        dataFile = open(self.storeFile,'wt')
        firstR=True
        for root, dirs, files in os.walk(self.directory): #does an iterative search
            for file in files:
                if file == self.paramFile:
                    if firstR:
                        csv=self.cleanRows(os.path.join(root, file),firstR)
                        firstR=False
                    csv=csv+self.cleanRows(os.path.join(root, file),firstR)
        
        dataFile.write(csv)
        dataFile.close()
        print('\nData stored correctly')
        
    def cleanRows(self,fname,firstRow):
        """
        Opens the file fname (text) and returns a string, either the first row
        (if firstRow=True) of a csv data file containing the column names,
        or a row with numerical values separated with commas
        """
        rowTop='Location,' #string for top row
        row=fname.replace('/'+self.paramFile,'')+',' #generic string afterwards
        file = open(fname,'rt')  #read text file   
        tmp=file.readlines()
        if firstRow:
            for line in tmp:
                value=line.split(sep='!')
                strB=value[1]
                #cleaning strings
                for tup in self.headerReplaceTup:
                    strB=strB.replace(tup[0],tup[1])
                rowTop=rowTop+strB+','
            return rowTop+'\n'
        else:
            for line in tmp:
                value=line.split(sep='!')
                strA=value[0]
                #cleaning strings
                for tup in self.bodyReplaceTup:
                    strA=strA.replace(tup[0],tup[1])
                if '.' in strA:
                    row=row+str(float(strA))+','
                else:
                    row=row+str(int(strA))+','
            return row+'\n'

mydata=simulationData()
mydata.fileSearch()