# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:48:06 2017
state lifetime analysis
input: state sequence, state number
output: lifetime of each state

@author: chord
"""
#from matplotlib import pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

def life_time(decoded,n):
    l=len(decoded)
#    states=range(n)
#    stp=0                   #start positon
#    enp=0                   #end positon
    life_t=([],[],[],[])           #storing lifetime
    trans=np.zeros((n,n))   #recording transition frequency
    temps=n+1               # temp state
    i=0
    while i<l-1:
#        print(i)
        temps=decoded[i]
        j=i
#        print(j)
        while (decoded[j]==temps)& (j<l-1):
            j=j+1
            trans[temps][temps]=trans[temps][temps]+1
#            if j>l-1:
#                break
        trans[temps][temps]=trans[temps][temps]-1
        life_t[temps].append(j-i)
        nst=decoded[j]
        trans[temps][nst]=trans[temps][nst]+1
        i=j
        temps=nst
    for i in range(n):
        trans[i]=trans[i]/sum(trans[i])
        
    return (life_t,trans)
#decoded=[1,1,0,0,0,2,2,2,2,0,0,1,0,1,2]
#[s,t]=life_time(decoded,3)
#print(s,t) 

def decay_line(life_t):
    bins = np.arange(0, max(life_t), max(life_t)/201); 
    cnt = plt.hist(life_t, bins)
    decay_l=[]
    sumt=sum(cnt[0])
    tim=cnt[1][0:199]
    for i in range(199):
#        print(i,sum(cnt[0][i:199])/sumt)
        decay_l.append(sum(cnt[0][i:199])/sumt)
    return (tim,decay_l)
