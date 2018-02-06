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
import matplotlib.pyplot as plt

comment = []
pos_count = 0
neg_count = 0

for line_data in open("请输入data_keywords.dat的目录"):
    
    comment = line_data
    
    s = SnowNLP(comment)
    rates = s.sentiments    
    
    if (rates >= 0.5):
        pos_count += 1

    elif (rates < 0.5):
        neg_count += 1
    
    else :
        pass


labels = 'Positive Side\n(eg. pray,eulogize and suggestion)', 'Negative Side\n(eg. abuse,sarcasm and indignation)'
fracs = [pos_count,neg_count]
explode = [0.1,0] # 0.1 凸出这部分，
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
#autopct ，show percet

plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)

plt.savefig("emotions_pie_chart.jpg",dpi = 360)
plt.show()
