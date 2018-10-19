#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:19:45 2018

This code is adapted from the C# example given here:
https://support.smartbear.com/articles/testcomplete/unit-testing/

@author: Leo
"""
import unittest #using TestCase
from nameExtractor import NameExtractor

class testNameExtractor(unittest.TestCase):
    """Tests for `nameExtractor.py`."""

    def test_rule1(self):
        rule1=NameExtractor("Mr John Greench Brown, PhD")
        self.assertTrue(rule1.mTitle == "Mr", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "John", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "Greench", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Brown", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "PhD", "Suffix is not correct")
        
    def test_rule2(self):
        rule1=NameExtractor("Mr.    John Brown")
        self.assertTrue(rule1.mTitle == "Mr", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "John", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Brown", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        rule1=NameExtractor("John Brown")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "John", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Brown", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        
    def test_rule3(self):
        rule1=NameExtractor("John-Martin Brown")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "John-Martin", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Brown", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        rule1=NameExtractor("Mr.    John Brown-II")
        self.assertTrue(rule1.mTitle == "Mr", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "John", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Brown-II", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")     
        
    def test_rule4(self):
        rule1=NameExtractor("Brown")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Brown", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        rule1=NameExtractor("Smith")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Smith", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        
    def test_rule5(self):
        rule1=NameExtractor("Mr. Smith")
        self.assertTrue(rule1.mTitle == "Mr", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Smith", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        rule1=NameExtractor("Capt. Blackmore")
        self.assertTrue(rule1.mTitle == "Capt", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Blackmore", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        rule1=NameExtractor("Mrs Young")
        self.assertTrue(rule1.mTitle == "Mrs", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Young", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        
    def test_rule6(self):
        rule1=NameExtractor("Kate More")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "Kate", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "More", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        rule1=NameExtractor("Capt. Blackmore")
        self.assertTrue(rule1.mTitle == "Capt", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Blackmore", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")
        rule1=NameExtractor("Pete Blackberry Mitchell")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "Pete", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "Blackberry", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Mitchell", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "", "Suffix is not correct")  
        
    def test_rule7(self):
        rule1=NameExtractor("Miss Kate More, PhD")
        self.assertTrue(rule1.mTitle == "Miss", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "Kate", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "More", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "PhD", "Suffix is not correct")
        rule1=NameExtractor("Peter Blackberry Mitchell, Esq")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "Peter", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "Blackberry", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "Mitchell", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "Esq", "Suffix is not correct")
  
    def test_rule8(self):
        rule1=NameExtractor("Kate More, PhD")
        self.assertTrue(rule1.mTitle == "", "Title is not correct")
        self.assertTrue(rule1.mFirstName == "Kate", "First Name is not correct")
        self.assertTrue(rule1.mMiddleName == "", " Middle Name is not correct")
        self.assertTrue(rule1.mLastName == "More", "Last Name is not correct")
        self.assertTrue(rule1.mSuffix == "PhD", "Suffix is not correct")
        
if __name__ == '__main__':
    unittest.main()

