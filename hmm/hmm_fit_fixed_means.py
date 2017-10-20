# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:09:49 2017

@author: chord
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:35:19 2017
hmm fit of a trace
input:
    csv data
    estimated mu
    estimated transtion matrix
output:
    decoded lifetime & parameter
    fitting score
    
@author: chord
"""
from matplotlib import pyplot as plt
import numpy as np
from hmmlearn import hmm
import csv
from lifetime_cal_v1 import life_time
from lifetime_cal_v1 import accu_line as al
from scipy.optimize import curve_fit 
from scipy import signal 
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
data=x['pdata']
a=data['Y_force'][0][0][0]
b=data['Ext'][0][0][0]
print(a)
aa=[]
bb=[]
for i in range(int(len(a)/5)-1):
    aa.append(sum(a[5*i:5*(i+1)])/5)
    bb.append(sum(b[5*i:5*(i+1)])/5)
high_force=max(a)
low_force=min(a)
#convolution
#win=signal.hann(5)
#aa=signal.convolve(a,win,mode='same')/sum(win)
#aa=[]
#for i in range(2,len(a)-3):
#    aa.append(np.mean(a[i-2:i+3]))
aa=[]
for i in range(int(len(a)/5)-1):
    aa.append(sum(a[5*i:5*(i+1)])/5)
# initial value
data = np.reshape(np.array(aa), [-1,1]);               #data for analysis
stat_num=2                                                  # number of states
bias=0.9                                                          # self transiton index
interval=(high_force-low_force)/(stat_num-1)
guess_m=[]
for ii in range(stat_num):
    guess_m.append(low_force+interval*ii)
#guess_mu=np.reshape(np.array(guess_m),[-1,1])
#init_tij=bias*np.eye(stat_num,stat_num)
#startprob=[1.0/stat_num]*int(stat_num)
#for ii in range(stat_num):
#    for jj in range(stat_num):
#        if init_tij[ii][jj]==0:
#            init_tij[ii][jj]=(1-bias)/(stat_num-1)       #finish setting init tij
#fitting
model = hmm.GaussianHMM(n_components=int(stat_num), covariance_type="full",n_iter=50, params='tcs',init_params="tcs")
#model.startprob_ = startprob
#model.transmat_ = tin
# for split4
#model.transmat_=np.array([[0.95,0.0,0,0.05],
#                          [0.0,0.9,0,0.1],
#                          [0,0.001,0.997,0.002],
#                          [0.001,0.005,0.004,0.990]])
# for split1
#model.transmat_=np.array( [[  0.98,   0.002 ,  0.011 ,  0.006,0.001  ],
# [  0.091  , 0.909 ,  0.00   ,0.00, 0.0],
# [  0.01 ,  0.00 ,  0.99,  0.00, 0.000],
# [   0.12 ,  0.01 ,    0.0,   0.80, 0.07],
# [  0.01 ,  0.0  , 0, 0.09,0.90],])
#model.transmat_=np.array( [[  0.9765,   0.0035 ,  0.01 ,  0.01,
#    0  , 0],
# [  0.11  , 0.850 ,  0.01   ,0.01, 0.02,  0.00],
# [  0.03 ,  0.00 ,  0.95,  0.0, 0.000 ,  0.02],
# [   0.04 ,  0.001 ,    0.05,   0.79, 0.05,   0.069],
# [  0.02 ,  0.01  , 0, 0.025, 0.94 ,  0.005],
# [  0.011  , 0.001  , 0.005 ,  0.002,0.001   ,0.98]])
#N12-4
#model.means_ = np.array([[5.55],[5.65],[5.85],[6.38]])
#N12-5
model.means_=np.array([[8.55],[9.76]])
#N12-5
#model.means_=np.array([[4.82],[4.92],[5.45]])
#N12-3
#model.means_ = np.array([[6.44],[6.63],[6.79],[7.38]])
#N12-2
#model.means_ = np.array([[6.27],[7.25],[7.37],[7.40],[7.73],[8.38]])
#model.startprob_=np.array([[0.1],[0.01],[0.887],[0.001],[0.001],[0.001]])
model.fit(data)
hidden_states = model.predict(data)
plt.figure()
plt.plot(data[000:2000])
hidden_means=[]
for i in range(len(hidden_states)):
    hidden_means.append(model.means_[hidden_states[i]])
plt.plot(hidden_means[00:2000])
plt.show()
decoded=model.decode(data) #state array
mu=[]
sigma=[]
for i in range(model.n_components):
    mu.append(model.means_[i])
    sigma.append(model.covars_[i])
temp_tij=model.transmat_
logL=model.score(data)
print(temp_tij)
[s,t]=life_time(list(decoded[1]),stat_num)
print(mu,t)
#plot decay_line
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
