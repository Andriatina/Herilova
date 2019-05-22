#!/usr/bin/env python
# coding: utf-8

# In[2]:


from __future__ import division


# In[2]:


neta_1_t_H=[0]
neta_1_t_T=[0]
neta_2_t_H=[0]
neta_2_t_T=[0]


# In[3]:


neta_1_t_H[0] = 1
neta_1_t_T[0] = 0
neta_2_t_H[0] = 0
neta_2_t_T[0] = 1


# In[4]:


p_1_strategy = ['H','T']
p_2_strategy = ['H','T']


# In[5]:


def neta_p_1(p_2_trate):
    weight_p1_for_p2H = 0
    weight_p1_for_p2T = 0
    if p_2_trate == 'H':
        weight_p1_for_p2H = weight_p1_for_p2H + 1
    if p_2_trate == 'T':
        weight_p1_for_p2T = weight_p1_for_p2T + 1
    return [weight_p1_for_p2H,weight_p1_for_p2T]

def neta_p_2(p_1_trate):
    weight_p2_for_p1H = 0
    weight_p2_for_p1T = 0
    if p_1_trate == 'H':
        weight_p2_for_p1H = weight_p2_for_p1H + 1
    if p_1_trate == 'T':
        weight_p2_for_p1T = weight_p2_for_p1T + 1
    return [weight_p2_for_p1H , weight_p2_for_p1T]


# In[6]:


def Choice_for_p1(S_11,S_12,SP):
    if S_11 < S12:
        return 'T'
    else:
        return 'H'
    if S_11==S12:
        return SP

def Choice_for_p2(S_11,S_12,SP):
    if S_11 < S12:
        return 'H'
    else:
        return 'T'
    if S_11==S12:
        return SP


# In[7]:


#print(p_2_choice(neta_2_t_H , neta_2_t_T))
W1 = [1,0]
W2 = [0,1]


# In[8]:


P = 4+2+3+4+25


# In[9]:


s = 0
for i in range(54):
    s = s + i


# In[10]:


P/s


# In[11]:


a = 1+2+2+2+2+2+3+4+5+6+6+6+6+6+7+8+9+30+11+12


# In[12]:


b= 1+2+2+2+2+2+3+4+5+6+6+6+6+6+7+8+9+10+10+10+10+10+11+12+13+14+14+14+14+14+15+16+17+18+18+18+18+18+19+20+21+22+22+22+22+22+23+24+25+26+26+26+26+26


# In[13]:


import pylab 


# In[14]:


import matplotlib.pyplot as plt


# In[15]:



s1 = [1,2,2,2,2,2,3,4,5,6,6,6,6,6,7,8,9,10,10,10,10,10,11,12,13,14,14,14,14,14,15,16,17,18,18,18,18,18,19,20,21,22,22,22,22,22]
s2 = [0,1,2,3,3,3,3,3,4,5,6,7,7,7,7,7,8,9,10,11,11,11,11,11,12,13,14,15,15,15,15,15,16,17,18,19,19,19,19,19,20,21,22,23,23,23]
T = 0
Pr_1 = []
Pr_2 = []

TT = []
for i in range(1,len(s1)+1):
    T = T  + i
    TT.append(T)
SS1 = 0 
SS2 = 0
SS = []
SSS = []
for i in range(len(TT)):
    SS1 = SS1 + s1[i]
    SS2 = SS2 + s2[i]
    SS.append(SS1)
    SSS.append(SS2)
    #print SS1
    #Pr_1.append(SS1/TT[i])

for i in range(len(TT)):
    Pr_1.append(SS[i]/TT[i])
    Pr_2.append(SSS[i]/TT[i])


# In[213]:


plt.figure(figsize=(12,7))
P1 = pylab.plot(TT,Pr_1, label = "Probability for the robot 1 to play H by the robot 2")
plt.rc('legend',**{'fontsize':12})
P2 = pylab.plot(TT,Pr_2, label = "Probability for the robot 2 to play H by the robot 1")
pylab.legend(loc='lower right')
P = P1+P2
pylab.ylabel('Probability')
pylab.xlabel('t')
plt.show(P)


# In[210]:


get_ipython().magic(u'pinfo pylab.legend')


# In[ ]:




