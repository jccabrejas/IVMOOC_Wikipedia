# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 20:26:52 2014

@author: JC
"""

import os
import glob

os.chdir(r'C:\Users\JC\Documents\categorylinks_snapshots')

category_file = open('category_names_by_id.txt', 'r')
output_file = open('category_names_by_name.txt', 'w')

cat_dict = {}

line = category_file.readline()
count = 0
while line != '':
    count += 1
    if count%100000 == 0:
        print count
        
    cat_id, cat_name = line.split()
    cat_dict[cat_name] = cat_id
    
    line = category_file.readline()
    
for key in sorted(cat_dict.iterkeys()):
    output_file.write("%s %s\n" % (key, cat_dict[key]))

output_file.close()
category_file.close()