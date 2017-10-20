# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 03:50:28 2017

@author: chord
"""
import math
col=['b','g','r','c','m','y','k']
###### raw data, filtered data, hidden data
#for i in range(21,30):
#    plt.figure()
#    xl=range(i*2000,(i+1)*2000)
#    raw_d=a[i*2000:(i+1)*2000]
#    s = [10 for n in range(len(raw_d))]
#    plt.scatter(xl,raw_d,s,[0.8,0.8,0.8])
#    x2=range(i*2000,(i+1)*2000,5)
#    plt.plot(x2,aa[i*400:(i+1)*400])
#    plt.plot(x2,hidden_means[i*400:(i+1)*400])

# gaussian emission
#def gaussian(x, mu, sigma):
#     return (1./(math.sqrt(2*math.pi)*sigma))*np.exp(-np.power((x - mu), 2.)/(2*sigma*sigma)) 
#x=arange(6,8.5,0.005)  
#plt.figure()
#for i in range(stat_num):
#    stat=sum(s[i])*gaussian(x,mu[i].item(),sigma[i].item())/len(aa)
#    plt.plot(x,stat)
    

plt.figure()
xl=range(len(a))
ss = [2 for n in range(len(a))]
plt.scatter(xl,a,ss,[0.8,0.8,0.8])
x2=range(0,len(a)-10,5)
plt.plot(x2,aa)
plt.plot(x2,hidden_means)