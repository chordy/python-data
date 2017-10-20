# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:52:28 2017
save data to txt
@author: chord
"""

from matplotlib import pyplot as plt
import numpy as np
from hmmlearn import hmm
import csv
from lifetime_cal import life_time
from lifetime_cal import accu_line as al
from scipy.optimize import curve_fit  
import scipy.io as io
def exp_func(x, k):  
    return 1-np.exp(-k * x)
def exp2_fun(x,k1,k2,a):
    return 1-a*np.exp(-k1*x)-(1-a)*np.exp(-k2*x)

acc=[[],[],[],[],[],[]]
tim=[[],[],[],[],[],[]]
for i in range(stat_num):
    plt.figure()
    tim[i],acc[i]=al(s[i])
#    plt.figure()
#    plt.plot(tim[i],acc[i])
#    popt, pcov = curve_fit(exp_func, tim[i], acc[i])
#    y1=[exp_func(iii,popt[0]) for iii in tim[i]]
#    popt2,pcov2=curve_fit(exp2_fun, tim[i],acc[i])
#    y2=[exp_func(iii,popt[0],popt[1],popt[2]) for iii in tim[i]]
#    plt.figure()
#    plt.plot(tim[i],acc[i])
#    plt.plot(tim[i],y1)
#    plt.plot(tim[i],y2)
#    plt.legend('data','exp1','exp2')
#    print(popt)
#    print(pcov)
#    f = open("split3_accu_1{}.csv".format(i),'w')
#
#    for j in range(len(tim[i])):
#        f.write("{}\t {}\n".format(tim[i][j], acc[i][j]))
#
#    f.close()
#f=open('n12_1_accu_sum_det1.csv','w')
#for j in range(len(tim[1])):
#    f.write('{}\t{}\t{}\t{}\t{}\n'.format(acc[0][j],acc[1][j],acc[2][j],acc[3][j],acc[4][j],acc[5][j]))
#    
#f.close()
#f=open('n12_1_t_sum_det1.csv','w')
#for j in range(len(tim[1])):
#    f.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(tim[0][j],tim[1][j],tim[2][j],tim[3][j],tim[4][j],tim[5][j]))
#    
#f.close()

tosave={}
tosave['tij']=t
tosave['mu']=mu
tosave['sigma']=sigma
tosave['rawdata']=a
tosave['hidden_means']=hidden_means
tosave['hidden_states']=hidden_states
tosave['filtered_data']=aa
tosave['filtered_ext']=bb
tosave['life']=s
tosave['acc_time']=tim
tosave['acc']=acc
io.savemat('n12_16_data',tosave)