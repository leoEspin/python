#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:19:45 2018
The Name Extractor takes the text input of an English/American proper name
(i.e. "Mr. John Smith") and extracts the following information from it:

Title (i.e. "Mr")
First Name (i.e. "John")
Middle Name (blank in sample case)
Last Name (i.e. "Smith")
Suffix (blank in sample case, could be Jr, II, PhD, DDS, etc)

This code is adapted from the C# example given here:
https://support.smartbear.com/articles/testcomplete/unit-testing/

@author: Leo
"""

class NameExtractor:
    mFullName = ''
    mTitle = ''
    mFirstName = ''
    mMiddleName = ''
    mLastName = ''
    mSuffix = ''
    mWords = ''
    separators=[',', '.', ':']
    TitleList=['Mr','Ms','Miss','Dr','Mrs','Fr','Capt','Lt','Gen',
               'President','Sister','Father','Brother','Major']
    SuffixList=['DDS','CFA','CEO','CFO','Esq','CPA','MBA','PhD',
                'MD','DC','Sr','Jr','II','III','IV']
    
    def __init__(self,*string):
        if len(string)>0:
            self.mFullName = str(string[0]) #have to convert the tuple first
            self.parseName()    
            
    def extractWords(self):
        if self.mFullName != '':
            words=self.mFullName.split()
            for i in range(len(words)): 
                for char in self.separators:
                    words[i]=words[i].replace(char,'')
            self.mWords=words
        else:
            self.parseName()
    
    def parseName(self):
        if self.mFullName != '':
            self.extractWords()
            self.FindTitle()
            self.FindSuffix()
            self.FindLastName()
            self.FindFirstName()
            self.FindMiddleName()
        else:
            self.mFullName = input('A name has to be provided first: ')
            self.parseName()
    
    def FindTitle(self):
        if self.mWords != '':
            if self.mWords[0] in self.TitleList:
                self.mTitle = self.mWords[0]
                self.mWords.pop(0)   
                
    def FindSuffix(self):
        if self.mWords != '':
            if self.mWords[-1] in self.SuffixList:
                self.mSuffix = self.mWords[-1]
                self.mWords.pop(-1)
                
    def FindLastName(self):
        length = len(self.mWords)
        if length == 1:
            self.mLastName=self.mWords[0]
            self.mWords.pop(0)
        elif (length == 2):
            self.mLastName=self.mWords[1]
            self.mWords.pop(1)
        elif (length == 3):
            self.mLastName=self.mWords[2]
            self.mWords.pop(2)
            
    def FindFirstName(self):
        if len(self.mWords) >0:
            self.mFirstName=self.mWords[0]
            self.mWords.pop(0)
            
    def FindMiddleName(self):
        if len(self.mWords) >0:
            self.mMiddleName=self.mWords[0]
            
