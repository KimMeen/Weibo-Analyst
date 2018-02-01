#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:59:46 2018
@author: Ming JIN
"""
#from snownlp import sentiment
#import numpy as np
from snownlp import SnowNLP
#from snownlp.sentiment import Sentiment

comment = []

array1 =[]
array2 =[]

count_num = 0
count_sum=200
  
for line_data in open("eva_data.dat"):
    
    comment = line_data
    
    s = SnowNLP(comment)
    rates = s.sentiments    
    
    if (rates >= 0.5):
        eva_label = 1
     
    else:
        eva_label = -1
    
    eva = str(eva_label)
    
    f = open("eva_result.dat", "a+")
    f.write(eva)
    f.write('\n')
    f.close()

for line1 in open("eva_label.dat"):
    array1.append(line1)
    
for line2 in open("eva_result.dat"):
    array2.append(line2)

for i in range(0,200):
    
    if (array1[i] == array2[i]):
        
        count_num += 1
        
correct_rate = count_num / count_sum

print(correct_rate)