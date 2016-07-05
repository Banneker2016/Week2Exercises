# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 09:50:14 2016

@author: jgarciamejia
"""

## COMMENT ALL THE CODE NICELY AFTER YOU ARE DONE

import matplotlib
from matplotlib import pyplot as plt
import numpy as np

#configure matplotlib sans-serif math for prettier plots :) 
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = [\
  r'\usepackage{siunitx}',\
  r'\sisetup{detect-all}',\
  r'\usepackage{avant}',\
  r'\usepackage{sansmath}',\
  r'\sansmath']

def my_prior_attempt(B):
    """
    Takes an array of biases between 0 to 1
    Prints a histogram with the distribution of biases - normalized
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
    Returns a prior. Right now the prior is a uniform distribution
    """
    return 1

# Run to test above code
#Bt = np.linspace(0,1,100)
#my_prior_attempt(Bt)


def likelihood_attempt(B, N, K): ## should be a y = x looking plot 
    """
    Likelihood is defined as the probability of obtaining a given data set
    given a hypothesis, where the hyporthesis is encoded in a bias factor. 
    As an example, if we flip a coin we can either get heads-H or tails-T. 
    So the likelihood for one coin flip will be given by:
    
    P({D} = H | B) = B
    P({D} = T | B) = 1 - B
    
    This function takes:
    - B: bias
    - K: amount of heads
    - N: total amount of flips
    
    Returns the likelihood of the data set or the functional form of P({D}|B,N,K,I)
    """
    return B**K * (1 - B)**(N - K)

def likelihood2(D, B):
    """
    Takes a data set array of H and T (or 1 and 0, respectively),
    determines K & N- K, and returns the likelihood for the given B, K and N
    """
    K = len([ heads for heads in D if heads == 1 or heads == 'H'])
    NminK = len([ tail for tail in D if tail == 0 or tail == 'T'])
    return B**K * (1 - B)**NminK

    
def posterior(D,B):
    """
    Recall from Bayes Theorem
    P(Hypothesis|Data, Information) = P(Hyp|Info) * P(Data|Hyp,Info) / P(Data|Info)
    In English
    Posterior = Prior * Likelihood / NormalizationConstant

    This function:
    Takes an array of coin flips (H and T or 1 and 0, respectively) and a bias B
    Returns the unnormalized posterior
    
    """
    # obtain the prior for the hypothesis
    prior = my_prior2(B)
    # obtain the likelihood
    likel = likelihood2(D,B)
    # plot the posterior 
    # return posterior
    return prior * likel

# plot P(B | N, K)
    
def plotposterior(D):
    """
    """
    # generate 10 evenly spaced numbers betweeon 0 and 1
    B = np.linspace(0,1,50) ## hardcoded number of points shown
    # initialize a posterior list
    posterior_list = []
    # populate the posterior list
    for number in B:
        posterior_list.append(posterior(D,number))
    # plot the posterior
    # initialize figure and axes
    fig = plt.figure(figsize=(4,4)) 
    ax1 = fig.add_axes([0.1,0.15,0.88,0.80]) # rectangle: left, bottom, width, height
    # plot data 
    plt.plot(B,posterior_list, '+', markersize=12, color = 'c', markeredgewidth=4)
    # labels
    ax1.set_xlabel(r'\textbf{Bias (B)}', fontsize=16)
    ax1.set_ylabel(r'\textbf{Posterior P(B \textbar N,K)}', fontsize=16)
    ax1.set_title(r'\textbf{Unnormalized PDF}', fontsize=18)
    # modify axes to make the ticks and spines thicker
    ax1.tick_params(axis='both',which='major',length=8,width=2,labelsize=16)
    [ii.set_linewidth(2) for ii in ax1.spines.itervalues()] ## this is to modify the spine -> 
    ## which is the border of the plot and make it thicker - I do width 2
    
    # call legend and show plot
    #plt.legend(loc = 'upper left')
    plt.show()
    return posterior_list
    

data_set1 = ['H']
data_set2 = ['H', 'T']
data_set3 = ['H', 'T', 'T']
plotposterior(data_set1)
plotposterior(data_set2)
plotposterior(data_set3)

# Prof. Johnson one of most cited papers uses this: what is the bias of having a planet?