# Created by Vishal Reddy Mandadi on 23-09-2021
# Q7 of assignment1 SMAI
import numpy as np
import matplotlib.pyplot as plt

def gen_random_nos(n=500):
    random_nos=np.random.uniform(low=0.0, high=1.0, size=(500, 1))
    sum_of_nos=np.sum(random_nos, axis=0)
    return sum_of_nos

def plot_area_norm_hist(num_arr_np_ar, no_of_bins):
    fig, ax = plt.subplots()
    x, bins, p=ax.hist(num_arr_np_ar, bins=no_of_bins, density=True)# density=True is for normalization
    ax.set(xlabel ='Random numbers', ylabel ='Frequency',
       title ='Normalized Histogram (area under the curve=1)')
    plt.savefig(fname='q7_normalized_hist.png')

if __name__=="__main__":
    num_arr = []
    bin_size=1
    no_of_calls=50000
    for i in range(no_of_calls):
        num_arr.append(gen_random_nos())
        #print("Random nos sum: {}".format(gen_random_nos()))
    num_arr_np = np.array(num_arr, dtype=float)
    no_of_bins = int((np.amax(num_arr_np)-np.amin(num_arr_np))/bin_size)
    plot_area_norm_hist(num_arr_np, no_of_bins)
    plt.show()
    #plt.show()
    #print(bins)
    #plt.savefig(fname='normalized_hist.png')
    #plt.savefig('normalized_hist.png')
    # Plotting histograms

        
    