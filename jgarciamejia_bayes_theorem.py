# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 09:50:14 2016

@author: jgarciamejia
"""

#import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def my_prior(B):
    """
    takes an array with biases from 0 to 1
    returns an array of prior probability P(B|I)
    """
    #prior = np.histogram(B,10)
    #x_prior = np.linspace(0,1,len(B))
    
    plt.figure()
    plt.ylim(0, 1.1)
    #ax1 = fig.add_axes([0.1,0.3, 0.8,0.7])  # rectangle: left, bottom, width, height
    #print B, B/(np.amax(B))
    plt.hist(B, normed = True)
    plt.show()
    return 
    
def my_prior2(B):
    """
    returns a probability density
    """
    return 1
    #return prior
#Bt = np.linspace(0,1,100)
#my_prior(Bt)


def likelihood(D, B, N, K): ## should be a y = x looking plot 
    """
    Likelihood is defined as the probability of obtaining a give data set
    given a hypothesis, where the hyporthesis is encoded in a bias factor so 
    for example if we flip a coin we can either get heads-H or tails-T. 
    So the likelihood
    
    P({D} = H | B) = B
    P({D} = T | B) = 1 - B
    
    This function
    takes a data array D and a bias B  and returns the likelihood
    """
    return B**K * (1 - B)**(N - K)
    #if D:
    #    return B
    #else:
    #   return (1 - B)

# The functional form of P({D}|B,N,K,I) = B**K (1 - B)**(N - K)
# Find code that returns posterior

def likelihood2(D, B):
    """
    Same as above except this function generates a random K
    H = 1
    T = 0
    """
    K = len([ heads for heads in D if heads == 1 or heads == 'H'])
    NminK = len([ tail for tail in D if tail == 0 or tail == 'T'])
    return B**K * (1 - B)**NminK


def posterior(D,B,N,K):
    """
    Feed it an array of data points D and an array of biases B
    As well as an amount of flips N and an amount of heads K
    
    Return the posterior given a data set, the prior and the likelihood
    """
    # obtain the prior for the hypothesis
    prior = my_prior2(B)
    # obtain the likelihood
    likel = likelihood(D,B,N,K)
    # return prior times likelihood
    return prior * likel
    # return posterior
    
def posterior2(D,B):
    """
    Feed it an array of data points D and an array of biases B
    As well as an amount of flips N and an amount of heads K
    
    Return the posterior given a data set, the prior and the likelihood
    """
    # obtain the prior for the hypothesis
    prior = my_prior2(B)
    # obtain the likelihood
    likel = likelihood2(D,B)
    # plot the posterior 
    # return posterior
    return prior * likel

# plot P(B | N, K)
    
def plotposterior(D,B):
    # generating 10 evenly spaced numbers betweeon 0 and 1
    B = np.linspace(0,1,10) ## hardocoded 10
    # initialize a posterior list
    posterior_list = []
    # populate the posterior list
    for number in B:
        posterior_list.append(posterior2(D,number))
    # plot the posterior list 
    plt.plot(B,posterior_list)
    plt.show()
    
    return posterior_list
    

data_set = ['H']

#plotposterior(data_set,0.5)

"""
if d:
    return b
else: 
    return (1-b)
"""
### for every value of B the likelihood of getting B is 
# Johnson most cited papers what is the bias of having a planet