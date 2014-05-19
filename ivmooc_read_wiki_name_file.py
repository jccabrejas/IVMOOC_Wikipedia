# -*- coding: utf-8 -*-
"""
Created on Tue Apr 01 20:56:01 2014

@author: JC

read wiki_names.txt and extract categories to a separate file
wiki_names.txt                     category_names.txt
6 AmericanSamoa                    690070 Category:Futurama
8 AppliedEthics                    690451 Category:World_War_II
10 AccessibleComputing             ...
...
690070 Category:Futurama
...
690451 Category:World_War_II
...

"""

import os
import glob

os.chdir(r'C:\Users\JC\Documents\categorylinks_snapshots')
myfile = open('wiki_names.txt','r')
category_file = open('category_names.txt', 'w')

count = 0
line = myfile.readline()
page_id, page_name = line.split()

while line != '':
    if 'Category:' in line:
        category_file.write(line)
    prev_id = int(page_id)
    page_id, page_name = line.split()
    if page_id <= prev_id:
        print prev_id, page_id, page_name
    count += 1
    if count%100000 == 0:
        print count
    line = myfile.readline()

myfile.close()
category_file.close()