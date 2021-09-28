# Created by Vishal Reddy Mandadi on 23-09-2021
# Q3 SMAI assignment 1
# Generating plots for normal and uniform distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

def normal_pdf(x_axis, mean, sd):
    return norm.pdf(x_axis, mean, sd)

def uniform_pdf(x=np.array([0], dtype=float), a=1, b=5):
    pdf = []
    for i in x:  
        if i <= b and i >= a:
            pdf.append(1/(b-a))
        else:
            pdf.append(0)
    return np.array(pdf, dtype=float)
  
# Plot between -5 and 10 with .001 steps.
x_axis = np.arange(-5, 10, 0.01)

# Calculating mean and standard deviation
mean = 3 # statistics.mean(x_axis)
sd = np.sqrt(4/3) #statistics.stdev(x_axis)

y_uniform = uniform_pdf(x=x_axis, a=1, b=5)
y_gaussian = normal_pdf(x_axis, mean, sd)

fig, ax = plt.subplots()
  
ax.set(xlabel ='Numbers', ylabel ='PDF',
       title ='Probability Distribution curves of uniform and normal distributions \nwith same mean(3) and variance(4/3)')

ax.plot(x_axis, y_uniform, color='r', label='uniform distribution')
ax.plot(x_axis, y_gaussian, color='g', label='gaussian distribution')
plt.legend()

# plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.savefig(fname='pdfs_of_different_distributions.png')
plt.show()
print(mean, sd)