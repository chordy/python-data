# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:32:39 2017

@author: chord
"""
import random 
from matplotlib import pyplot as plt
import numpy as np
from hmmlearn import hmm
startprob = np.array([0.6,0.4])
# The transition matrix, note that there are no transitions possible
# between component 1 and 3
transmat = np.array([[0.9, 0.1],
                     [0.2, 0.8]])
# The means of each component
means = np.array([[40],
                  [10]])
model = hmm.GaussianHMM(n_components=2, covariance_type="full")
model.startprob_ = startprob
model.transmat_ = transmat
model.means_ = means
#generate 1D time sequence
data=[]
s=[]
s.append(1)
ss=1
for i in range(200):
    tmp=random.random()
    if ss==1:
        if tmp <0.95:
            s.append(1)
        else :
            s.append(0)
            ss=0
    else:
        if tmp<0.9:
            s.append(0)
        else:
            s.append(1)
            ss=1
for i in range(len(s)):
    if s[i]==1:
        data.append(10*random.random()+35)
    else:
        data.append(10*random.random())
pydata = np.reshape(np.array(data), [-1,1]);
#x=np.array(data)
model.fit(pydata)
hidden_states = model.predict(pydata)
plt.plot(pydata)
#plt.plot(hidden_states)
for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("mean = ", model.means_[i])
    print("var = ", np.diag(model.covars_[i]))
    print()
hidden_means=[]
for i in range(len(hidden_states)):
    hidden_means.append(model.means_[hidden_states[i]])
plt.plot(hidden_means)
plt.show()
