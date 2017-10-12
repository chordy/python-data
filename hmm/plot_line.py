# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:26:47 2017

@author: chord
"""
#import scipy
import matplotlib
matplotlib.rcParams.update({'font.size': 22})
import matplotlib.pyplot as plt
f=open('D:/data.txt','r')
print(f)
lines=f.readlines()
t=[]
p=[]
p1=[]
p2=[]
for line in lines:
    line=line.rstrip()
    #print(line)
    line=line.split('\t')
    #print(line)
    t.append(float(line[0]))
    p.append(float(line[1]))
    p1.append(float(line[2]))
    p2.append(float(line[3]))
    
#print(t)
#print(p)
#fig = plt.figure() 
#fig.show()
plt.plot(t,p,label='blank')
plt.plot(t,p1,label='ss non-PAM')
plt.plot(t,p2,label='ss PAM-rich')
plt.xlabel('Time(min)')
plt.ylabel('Vanished fraction')
plt.legend(loc='lower right')
