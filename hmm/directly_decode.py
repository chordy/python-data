# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:12:30 2017

@author: chord
"""

from matplotlib import pyplot as plt
import numpy as np
from hmmlearn import hmm
import csv
from lifetime_cal import life_time
a=[]
#read in data / filter/ hist
with open('testdata.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        a.append(float(row[0]))
# filter means
aa=[]
for i in range(int(len(a)/5)-1):
    aa.append(sum(a[5*i:5*(i+1)])/5)
bins = np.arange(min(aa), max(aa), 0.002); #浮点数版本的range
#bins = np.arange(9, 10, 0.02); 
plt.figure()
plt.hist(aa,bins)
plt.xlabel('Force pN')
plt.ylabel('Count')
plt.show()