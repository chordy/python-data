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
from scipy import signal
a=[]
with open('testdata6.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        a.append(float(row[0]))
high_force=max(a)
low_force=min(a)
#convolution
#win=signal.hann(100)
#b=signal.convolve(a,win,mode='same')/sum(win)
# initial value
data = np.reshape(np.array(a[15000:20000]), [-1,1]);               #data for analysis
stat_num=3                                                                # number of states
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
model = hmm.GaussianHMM(n_components=int(stat_num), covariance_type="full")
model.startprob_ = startprob
model.transmat_ = init_tij
model.means_ = guess_mu
model.fit(data)
hidden_states = model.predict(data)
plt.figure()
plt.plot(data)
hidden_means=[]
for i in range(len(hidden_states)):
    hidden_means.append(model.means_[hidden_states[i]])
plt.plot(hidden_means)
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
#
#plt.figure()
#plt.hist(s[0])
#plt.figure()
#plt.hist(s[1])
#plt.figure()
#plt.hist(s[2])