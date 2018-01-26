#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:59:46 2018

@author: Ming JIN
"""
from snownlp import sentiment

sentiment.train('negative_dict.txt', 'positive_dict.txt')
sentiment.save('sentiment.marshal')