#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import os

path = os.getcwd()
file_name = os.listdir(path)
prefix = raw_input("Please Input the prefix you wanna remove:")
file_name_new = []
for name in file_name:
    if prefix not in name:
        continue
    print name
    new_name = name.split(prefix)[1]
    file_name_new.append(new_name)
    os.system('rename %s %s'%(name,new_name))
    print new_name
    
