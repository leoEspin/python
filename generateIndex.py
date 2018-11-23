#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:14:58 2018
Script for generating the index file for the documentation folder
@author: Leo Espin
"""
import os
list=''
for file in os.listdir("docs/"):
    if file.endswith(".html"):
        list=(list+'* ['+file.split('.')[0]+
        '](https://leoespin.github.io/python/' +file +')\n')

with open('docs/index.md', "w") as index:
    #index.write('<center> <h1>Machine learning notes</h1>A collection of python codes</center>\n')
    #index.write('\n')
    index.write('Project maintained by [Leo Espin](https://github.com/leoEspin), Hosted on GitHub Pages\n\n')
    index.write('This folder contains useful notes about my machine learning projects:\n')
    index.write(list)
