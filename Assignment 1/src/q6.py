# Created by Vishal Reddy Mandadi on 23-09-2021
# Q6 SMAI Assignment 1

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
from scipy.stats import norm, rayleigh, expon
import statistics

def uniform_to_normal(x, mu=0.0, sd=3.0): 
    # mu - mean, sd - standard_deviation
    return norm.ppf(x, loc=mu, scale=sd)

def uniform_to_rayleigh(x, mu=0.0, sd=1.0):
    return rayleigh.ppf(x, mu, sd)

def uniform_to_exponential(x, mu=2/3, sd=2/3):
    return expon.ppf(x, scale=sd)

if __name__=="__main__":
    # generate 10,000 rand nos
    rand_nos = np.random.uniform(low=0.0, high=1.0, size=(10000, 1))

    # Map then to Normal Distribution
    mean=0.0
    sd=3.0
    normal_nos = []
    normal_nos=uniform_to_normal(rand_nos, mu=mean, sd=sd)
    #print("Normal Nos: {}".format(normal_nos))
    bin_size=0.5
    no_of_bins = int((np.amax(normal_nos)-np.amin(normal_nos))/bin_size)
    fig, axes = plt.subplots(1, 1)
    axes.hist(normal_nos, bins=no_of_bins, density=True, label='using inverse CDF')
    axes.set_title("Normal Distribution,\n mu=0, sd=3.0")
    x_axis = np.arange(-20, 20, 0.01)
    axes.plot(x_axis, norm.pdf(x_axis, mean, sd), color='r', label='using PDF')
    axes.legend()
    plt.savefig("q6_normal.png")
    #plt.show()

    # Map them to Rayleigh Distribution
    mean=0.0
    sd=1.0
    rayleigh_nos = []
    rayleigh_nos=uniform_to_rayleigh(rand_nos, mu=mean, sd=sd)
    bin_size=0.05
    no_of_bins = int((np.amax(rayleigh_nos)-np.amin(rayleigh_nos))/bin_size)
    fig, axes = plt.subplots(1, 1)
    axes.hist(rayleigh_nos, bins=no_of_bins, density=True, label='using inverse CDF')
    axes.set_title("Rayleigh Distribution,\n mu=0, sd=1.0")
    x_axis = np.arange(-0, 10, 0.01)
    axes.plot(x_axis, rayleigh.pdf(x_axis, mean, sd), color='r', label='using PDF')
    axes.legend()
    plt.savefig("q6_rayleigh.png")
    #plt.show()

    # Map them to exponential distribution
    lmbda = 1.2 # 1.5
    mean = 1/lmbda
    sd = 1/lmbda
    exp_nos = []
    exp_nos=uniform_to_exponential(rand_nos, mu=mean, sd=sd)
    bin_size=0.045
    no_of_bins = int((np.amax(exp_nos)-np.amin(exp_nos))/bin_size)
    fig, axes = plt.subplots(1, 1)
    axes.hist(exp_nos, bins=no_of_bins, density=True, histtype='stepfilled', label='using inverse CDF')
    axes.set_title("Exponential Distribution,\n lambda=1.5")
    x_axis = np.arange(0, 10, 0.01)
    axes.plot(x_axis, expon.pdf(x_axis, scale=sd), color='r', label='using PDF')
    axes.legend()
    plt.savefig("q6_exp.png")
    #plt.show()


