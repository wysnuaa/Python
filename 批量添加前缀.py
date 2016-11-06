#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import os

path = os.getcwd()
file_name = os.listdir(path)
prefix = raw_input("Please Input the prefix name:")
file_name_new = []
for name in file_name:
    print name
    new_name = prefix + name
    file_name_new.append(new_name)
    os.system('rename %s %s'%(name,new_name))
    print new_name
    
