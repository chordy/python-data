# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 11:54:47 2017

@author: chord
"""

from matplotlib import pyplot as plt
import numpy as np
from hmmlearn import hmm
import csv
a=[]
with open('testdata.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        a.append(float(row[0]))
high_force=max(a)
low_force=min(a)

data = np.reshape(np.array(a[20000:30000]), [-1,1]);               #data for analysis
min_n=3
max_n=3                                               #number of states
bias=[0.9,0.001]  #state life time?
temp_bic=[]
temp_mu=[]
temp_traj=[]
temp_sigma=[]
temp_tij=[]
for n in range(max_n-min_n+1):
    for i in range(len(bias)):
        stat_num=n+min_n
        print(stat_num)
        interval=(high_force-low_force)/(stat_num-1)
        guess_m=[]
        for ii in range(stat_num):
            guess_m.append(low_force+interval*ii)
        guess_mu=np.reshape(np.array(guess_m),[-1,1])
        init_tij=bias[i]*np.eye(stat_num,stat_num)
        startprob=[1.0/stat_num]*int(stat_num)
        for ii in range(stat_num):
            for jj in range(stat_num):
                if init_tij[ii][jj]==0:
                    init_tij[ii][jj]=bias[i]/(stat_num-1)       #finish setting init tij
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
        for i in range(model.n_components):
            temp_mu.append(model.means_[i])
            temp_sigma.append(model.covars_[i])
        temp_tij.append(model.transmat_)
        logL=model.score(data)
print(temp_tij)


            
    