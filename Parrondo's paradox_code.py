#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import random as random
from __future__ import division


# ### Game A

# In[3]:


def flip_coin(round_number):
    loss = [0]
    win = [0]
    for i in range(round_number):
        a = random.random()
        if a <= 0.49:
            win.append(1)
        else:
            loss.append(1)
    
    E_loss = len(loss)/round_number
    E_win = len(win)/round_number
    l = [E_loss, E_win]
    return l


# In[4]:


def game_number(GN, round_number):
    LOSS = [0]
    WINN = [0]
    for i in range(GN):
        LOSS.append((flip_coin(round_number))[0])
        WINN.append((flip_coin(round_number))[1])
    return LOSS, WINN


# In[47]:


GN, round_number = 100, 10000
t = [i for i in range(GN+1)]
plt.figure(figsize=(12,7))
P1 = plt.plot(t, game_number(GN, round_number)[0], label = "Loss")
plt.rc('legend',**{'fontsize':8})
P2 = plt.plot(t, game_number(GN, round_number)[1], label = "Win")
P = P1+P2
plt.ylabel('Expectation')
plt.xlabel('Game number ')

plt.show(P)


# 

# In[30]:


plt.figure(figsize=(12,7))
line_up, = plt.plot(game_number(GN, round_number)[0], label='Line 2')
line_down, = plt.plot(game_number(GN, round_number)[1], label='Line 1')
plt.legend([line_up, line_down], ['Expectation(Loss) ', 'Expectation(Win)'],fontsize=20)
plt.ylabel('Expectation',fontsize=14)
plt.xlabel('Game number ',fontsize=14)


# ### Game B

# In[31]:


def Game_B(parties):
    loss = [0]
    win = [0]
    g = 0
    for i in range(parties):
        a = random.random()
        if g % 3==0:
            if a <= 0.09:
                win.append(1)
                g = g + 1
            else:
                loss.append(1)
                g = g - 1
        else :
            if a <= 0.74:
                win.append(1)
                g = g + 1
            else:
                loss.append(1)
                g = g - 1
    E_loss = len(loss)/round_number
    E_win = len(win)/round_number
    l = [E_loss, E_win]
    return l


# In[42]:


Game_B(100)


# In[43]:


def game_number2(GN, round_number):
    LOSS = [0]
    WINN = [0]
    for i in range(GN):
        LOSS.append((Game_B(round_number))[0])
        WINN.append((Game_B(round_number))[1])
    return LOSS, WINN


# In[45]:


plt.figure(figsize=(12,7))
line_up, = plt.plot(game_number2(GN, round_number)[0], label='Line 2')
line_down, = plt.plot(game_number2(GN, round_number)[1], label='Line 1')
plt.legend([line_up, line_down], ['Expectation(Loss) ', 'Expectation(Win)'],fontsize=20)
plt.ylabel('Expectation',fontsize=14)
plt.xlabel('Game number ',fontsize=14)


# ### Game AB

# In[48]:


def Game_AB(parties):
    loss = [0]
    win = [0]
    g = 0
    GAME = ['A','B']
    for i in range(parties):
        G = random.choice(GAME)
        if G == 'A':
            #----------------------------------#
            a = random.random()
            if g % 3==0:
                if a <= 0.09:
                    win.append(1)
                    g = g + 1
                else:
                    loss.append(1)
                    g = g - 1
            else :
                if a <= 0.74:
                    win.append(1)
                    g = g + 1
                else:
                    loss.append(1)
                    g = g - 1
        #----------------------------------#
        else:
            a = random.random()
            if a <= 0.49:
                win.append(1)
                g = g + 1
            else:
                loss.append(1)
                g = g - 1
    E_loss = len(loss)/round_number
    E_win = len(win)/round_number
    l = [E_loss, E_win]
    return l


# In[53]:


Game_AB(1000)


# In[54]:


def game_number3(GN, round_number):
    LOSS = [0]
    WINN = [0]
    for i in range(GN):
        LOSS.append((Game_AB(round_number))[0])
        WINN.append((Game_AB(round_number))[1])
    return LOSS, WINN


# In[58]:


GN, round_number = 100, 40000
plt.figure(figsize=(12,7))
line_up, = plt.plot(game_number3(GN, round_number)[0], label='Line 2')
line_down, = plt.plot(game_number3(GN, round_number)[1], label='Line 1')
plt.legend([line_up, line_down], ['Expectation(Loss) ', 'Expectation(Win)'],fontsize=20)
plt.ylabel('Expectation',fontsize=14)
plt.xlabel('Game number ',fontsize=14)


# In[ ]:




