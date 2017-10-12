# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy
import matplotlib.pyplot as plt
f=open('D:/data.txt','r')
print(f)
lines=f.readlines()
t=[]
p=[]
for line in lines:
    line=line.rstrip()
    #print(line)
    line=line.split('\t')
    #print(line)
    t.append(float(line[0]))
    p.append(float(line[1]))
    
print(t)
print(p)
plt.bar(t,p,color='r')
plt.xlabel('Time(min)')
plt.ylabel('Probablity')
plt.show()