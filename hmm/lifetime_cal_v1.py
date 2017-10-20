# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:48:06 2017
state lifetime analysis
input: state sequence, state number
output: lifetime of each state
modified in Oct 14, s1->s2->s3, delete very short s2, maybe form filtering

@author: chord
"""
#from matplotlib import pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

def life_time(decoded,n):
    l=len(decoded)
    ns=decoded
    for i in range(l-10):
        if (ns[i]!=ns[i+1])& (ns[i+1]!=ns[i+2]):
            ns[i+1]=ns[i]
    # remove short 4-5-4 ,specific for this sample,pre-crocess
#    i=1
#    while i<l-2:
##        print(i,ns[i],ns[i-1])
#        if (ns[i]==5) & (ns[i-1]==4):
##            print('i',i)
#            j=i+1
#            while ns[j]==5:
#                j=j+1
#            print(i,ns[j])
#            if ns[j]==4:
##                print('yes')
#                if j-i<10:
#                    for ll in range(i,j+1):
#                        ns[ll]=4
##                print(i,j,ns[i:j])
#            i=j+1
#        else :
#            i=i+1
            
        
#    states=range(n)
#    stp=0                   #start positon
#    enp=0                   #end positon
    life_t=([],[],[],[],[],[])           #storing lifetime
    trans=np.zeros((n,n))   #recording transition frequency
    temps=n+1               # temp state
    i=0
    while i<l-1:
#        print(i)
        temps=ns[i]
        j=i
#        print(j)
        while (ns[j]==temps)& (j<l-1):
            j=j+1
            trans[temps][temps]=trans[temps][temps]+1
#            if j>l-1:
#                break
        trans[temps][temps]=trans[temps][temps]-1
        life_t[temps].append(j-i)
        nst=ns[j]
        trans[temps][nst]=trans[temps][nst]+1
        i=j
        temps=nst
    for i in range(n):
        trans[i]=trans[i]/sum(trans[i])
        
    return (life_t,trans)
#ns=[1,1,0,0,0,2,2,2,2,0,0,1,0,1,2]
#[s,t]=life_time(ns,3)
#print(s,t) 

def decay_line(life_t):
    bins = np.arange(0, max(life_t), max(life_t)/201)
    cnt = plt.hist(life_t, bins)
    decay_l=[]
    sumt=sum(cnt[0])
    tim=cnt[1][0:199]
    for i in range(199):
#        print(i,sum(cnt[0][i:199])/sumt)
        decay_l.append(sum(cnt[0][i:199])/sumt)
    return (tim,decay_l)
def accu_line(life_t):
    # accumulative of life time
    bins=np.arange(0,max(life_t),max(life_t)/201)
    cnt=plt.hist(life_t,bins)
    acc_l=[]
    sumt=sum(cnt[0])
    tim=cnt[1][0:199]
    for i in range(199):
        acc_l.append(sum(cnt[0][0:i])/sumt)
    return(tim, acc_l)