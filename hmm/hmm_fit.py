# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:35:19 2017
hmm fit of a trace
input:
    csv data
output:
    fitted mu
    decoded hidden state
    fitting score
    
@author: chord
"""
from matplotlib import pyplot as plt
import numpy as np
from hmmlearn import hmm
import csv
from lifetime_cal import life_time
from lifetime_cal import accu_line as al
from scipy.optimize import curve_fit
from scipy.io import loadmat 
#from scipy import signal

def exp_func(x, k):  
    return 1-np.exp(-k * x)
def exp2_fun(x,k1,k2,a):
    return 1-a*np.exp(-k1*x)-(1-a)*np.exp(-k2*x)

#a=[]
#with open('testdata.csv','r') as f:
#    reader=csv.reader(f)
#    for row in reader:
#        a.append(float(row[0]))
x = loadmat('N12_16_split.mat')
data1=x['pdata']
a=data1['Y_force'][0][0][0]
b=data1['Ext'][0][0][0]
print(a)
aa=[]
for i in range(int(len(a)/5)-1):
    aa.append(sum(a[5*i:5*(i+1)])/5)
#aa=[]
#for i in range(2,len(a)-3):
#    aa.append(np.mean(a[i-2:i+3]))
high_force=max(a)
low_force=min(a)
#convolution
#win=signal.hann(100)
#b=signal.convolve(a,win,mode='same')/sum(win)
# initial value
data = np.reshape(np.array(aa), [-1,1]);               #data for analysis
stat_num=2                                                    # number of states
bias=0.9                                                          # self transiton index
interval=(high_force-low_force)/(stat_num-1)
guess_m=[]
for ii in range(stat_num):
    guess_m.append(low_force+interval*ii)
guess_mu=np.reshape(np.array(guess_m),[-1,1])
init_tij=bias*np.eye(stat_num,stat_num)
startprob=[1.0/stat_num]*int(stat_num)
for ii in range(stat_num):
    for jj in range(stat_num):
        if init_tij[ii][jj]==0:
            init_tij[ii][jj]=bias/(stat_num-1)       #finish setting init tij
#fitting
model = hmm.GaussianHMM(n_components=int(stat_num), covariance_type="full",n_iter=50,)
model.startprob_ = startprob
model.transmat_ = init_tij
model.means_ = guess_mu
model.fit(data)
hidden_states = model.predict(data)
plt.figure()
plt.plot(aa[2000:4000])
#plt.plot(data)
hidden_means=[]
for i in range(len(hidden_states)):
    hidden_means.append(model.means_[hidden_states[i]])
plt.plot(hidden_means[2000:4000])
plt.show()
decoded=model.decode(data) #state array
mu=[]
sigma=[]
for i in range(model.n_components):
    mu.append(model.means_[i])
    sigma.append(model.covars_[i])
temp_tij=model.transmat_
logL=model.score(data)
#print(temp_tij)
[s,t]=life_time(list(decoded[1]),stat_num)
#print(mu,t)
#
#plt.figure()
#plt.hist(s[0])
#plt.figure()
#plt.hist(s[1])
#plt.figure()
#plt.hist(s[2])
acc=[[],[],[],[],[],[]]
tim=[[],[],[],[],[],[]]
for i in range(stat_num):
    plt.figure()
#bins = np.arange(min(s[0]), max(s[0]), 5); #浮点数版本的range
    tim[i],acc[i]=al(s[i])
    popt, pcov = curve_fit(exp_func, tim[i], acc[i])
    y1=[exp_func(iii,popt[0]) for iii in tim[i]]
#    popt2,pcov2=curve_fit(exp2_fun, tim[i],dec[i])
#    y2=[exp_func(iii,popt[0],popt[1],popt[2]) for iii in tim[i]]
    plt.figure()
    plt.plot(tim[i],acc[i])
    plt.plot(tim[i],y1)
#    plt.plot(tim[i],y2)
#    plt.legend('data','exp1','exp2')
#    print(popt)
#    print(pcov)