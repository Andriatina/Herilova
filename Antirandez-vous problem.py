#!/usr/bin/env python
# coding: utf-8

# In[207]:


import matplotlib.pyplot as plt
import numpy as np
import random as random
from __future__ import division
import pylab


# In[208]:


Pos = {'s1':[1,1],'s2':[2,1],'s3':[3,1],'s4':[4,1],'s5':[1,2],'s6':[2,2],'s7':[3,2],'s8':[4,2],'s9':[1,3],'s10':[2,3],'s11':[3,3],'s12':[4,3]}
L_2 = L_1 = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12']



# In[209]:


def norm(point_1,point_2):
    d = np.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    return d


# In[210]:


w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
w_2_for_1 = {'s1':0,'s2':0,'s3':1,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}


# In[211]:


l1 = max([(w_1_for_2[i],i) for i in L_2])[1]
l2 = max([(w_2_for_1[i],i) for i in L_2])[1]


# In[214]:


#del d[key]
def Next_move(w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0},w_2_for_1 = {'s1':0,'s2':0,'s3':1,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}):
    l1 = max([(w_1_for_2[i],i) for i in L_2])[1]
    l2 = max([(w_2_for_1[i],i) for i in L_2])[1]
    d1 = []
    d2 = []
    Pos = {'s1':[1,1],'s2':[2,1],'s3':[3,1],'s4':[4,1],'s5':[1,2],'s6':[2,2],'s7':[3,2],'s8':[4,2],'s9':[1,3],'s10':[2,3],'s11':[3,3],'s12':[4,3]}
    for i in L_1:
        d1.append([norm(Pos[l1],Pos[i]),i])
        d2.append([norm(Pos[l2],Pos[i]),i])
    next_move_r1 = max(d1)[1]
    for i in range(len(d1)):
        if d2[i][1]== next_move_r1:
            del d2[i]
            break
    next_move_r2 = max(d2)[1]
    distance = norm(Pos[next_move_r1],Pos[next_move_r2])
    return [next_move_r1,next_move_r2,distance]

def updateWeight1( b = 's1',w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}):
    for i in L_2:
        if b == i:
            w_1_for_2[i] = w_1_for_2[i] + 1
    return w_1_for_2
def updateWeight2(a = 's1',w_2_for_1 = {'s1':0,'s2':0,'s3':1,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}):
    for i in L_2:
        if a == i:
            w_2_for_1[i] = w_2_for_1[i] + 1
    return w_2_for_1


# In[215]:


w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
w_2_for_1 = {'s1':0,'s2':1,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
def Dist(w_1_for_2,w_2_for_1,n):
    M = []
    distance = []
    L_2 = L_1 = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12']
    l1 = max([(w_1_for_2[i],i) for i in L_2])[1]
    l2 = max([(w_2_for_1[i],i) for i in L_2])[1]
    Pos = {'s1':[1,1],'s2':[2,1],'s3':[3,1],'s4':[4,1],'s5':[1,2],'s6':[2,2],'s7':[3,2],'s8':[4,2],'s9':[1,3],'s10':[2,3],'s11':[3,3],'s12':[4,3]}
    distance.append(norm(Pos[l1],Pos[l2]))
    for i in range(n):
        M.append(i)
        a = Next_move(w_1_for_2,w_2_for_1)[0]
        b = Next_move(w_1_for_2,w_2_for_1)[1]
        c = Next_move(w_1_for_2,w_2_for_1)[2]
        distance.append(c)
        w_1_for_2 = updateWeight1(b,w_1_for_2)
        w_2_for_1 = updateWeight2(a,w_2_for_1)
    return [M,distance]


# In[216]:


Dist(w_1_for_2,w_2_for_1,10)[1]
t = []
for i in range(len(Dist(w_1_for_2,w_2_for_1,1)[1])):
    t.append(i)
w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
w_2_for_1 = {'s1':0,'s2':1,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}


# In[ ]:





# In[217]:


from scipy.interpolate import spline

t = []
for i in range(len(Dist(w_1_for_2,w_2_for_1,50)[1])):
    t.append(i)

w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
w_2_for_1 = {'s1':0,'s2':1,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
plt.figure(figsize=(12,7))
P1 = pylab.plot(t,Dist(w_1_for_2,w_2_for_1,50)[1], label = "Distance between the two robots")
#P1 = spline(P1)
plt.rc('legend',**{'fontsize':12})
pylab.legend(loc='lower right')
pylab.ylabel('Distance')
pylab.xlabel('Period')
plt.show(P1)


# ## ---------------------------------------------------------------------------------------------------------------------##
# ### No argmax
# 

# In[218]:


#del d[key]
def Next_move2(w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0},w_2_for_1 = {'s1':0,'s2':0,'s3':1,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}):
    average = 2.0
    l1 = max([(w_1_for_2[i],i) for i in L_2])[1]
    l2 = max([(w_2_for_1[i],i) for i in L_2])[1]
    d1 = []
    d2 = []
    Pos = {'s1':[1,1],'s2':[2,1],'s3':[3,1],'s4':[4,1],'s5':[1,2],'s6':[2,2],'s7':[3,2],'s8':[4,2],'s9':[1,3],'s10':[2,3],'s11':[3,3],'s12':[4,3]}
    for i in L_1:
        d1.append([norm(Pos[l1],Pos[i]),i])
        d2.append([norm(Pos[l2],Pos[i]),i])
    d11 = [d1[i] for i in range(len(d1)) if d1[i][0]>=2]
    d12 = [d2[i] for i in range(len(d1)) if d2[i][0]>=2]
    next_move_r1 = random.choice(d11)
    next_move_r1 = next_move_r1[1]
    #d12 = [d12[i] for i in range(len(d12)) if d12[i][1] != next_move_r1]        
    next_move_r2 = random.choice(d12)
    next_move_r2 = next_move_r2[1]
    distance = norm(Pos[next_move_r1],Pos[next_move_r2])
    return [next_move_r1,next_move_r2,distance]




# In[219]:


def Dist2(w_1_for_2,w_2_for_1,n):
    M = []
    distance = []
    L_2 = L_1 = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12']
    l1 = max([(w_1_for_2[i],i) for i in L_2])[1]
    l2 = max([(w_2_for_1[i],i) for i in L_2])[1]
    Pos = {'s1':[1,1],'s2':[2,1],'s3':[3,1],'s4':[4,1],'s5':[1,2],'s6':[2,2],'s7':[3,2],'s8':[4,2],'s9':[1,3],'s10':[2,3],'s11':[3,3],'s12':[4,3]}
    distance.append(norm(Pos[l1],Pos[l2]))
    for i in range(n):
        M.append(i)
        a = Next_move2(w_1_for_2,w_2_for_1)[0]
        b = Next_move2(w_1_for_2,w_2_for_1)[1]
        c = Next_move2(w_1_for_2,w_2_for_1)[2]
        distance.append(c)
        w_1_for_2 = updateWeight1(b,w_1_for_2)
        w_2_for_1 = updateWeight2(a,w_2_for_1)
    return [M,distance]


# In[ ]:


t = []
for i in range(len(Dist2(w_1_for_2,w_2_for_1,50)[1])):
    t.append(i)

w_1_for_2 = {'s1':1,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
w_2_for_1 = {'s1':0,'s2':1,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0}
plt.figure(figsize=(12,7))
P1 = pylab.plot(t,Dist2(w_1_for_2,w_2_for_1,50)[1], label = "Distance between the two robots")
#P1 = spline(P1)
plt.rc('legend',**{'fontsize':12})
pylab.legend(loc='upper left')
pylab.ylabel('Distance')
pylab.xlabel('Period')
plt.show(P1)


# In[184]:


print len(d1)
print len (d2)
d11 = [d1[i] for i in range(len(d1)) if d1[i][0]>=2]
d12 = [d2[i] for i in range(len(d1)-1) if d2[i][0]>=2]
next_move_r1 = random.choice(d11)
next_move_r1 = next_move_r1[1]
d12 = [d12[i] for i in range(len(d12)) if d12[i][1] != next_move_r1]        
next_move_r2 = random.choice(d12)
next_move_r2 = next_move_r2[1]


# In[ ]:





# In[ ]:




