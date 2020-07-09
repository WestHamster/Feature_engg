import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

data = np.loadtxt("dataset.txt")
plt.hist(data)
plt.show()

#Centrality can be defined by average
"""def get_mean(x_input):
  sum = 0
  for x in x_input:
    sum += x
  return sum / len(x_input)
#print(get_mean([2,4,6,8]))
"""
mean = np.mean(data)
print("mean     data.mean()     np.average(data)")
print(mean,data.mean(),np.average(data))

#invoke data.mean() when working with pandas dataframe/ numpy array but not
#on list
#np.average(data) identical to mean but we can also pass in weights
print()
print()
#Median - sort from small to largest and then middle number
#If even no's then average of central two numbers (n/2 + n+1/2)

"""
def get_median(x_inp):
    mid = len(x_inp)//2
    if len(x_inp) %2 == 1:
        return sorted(x_inp)[mid]
    else:
        return 0.5 * np.sum(sorted(x_inp)[mid-1:mid+1])
print(get_median([5,4,2,1,2]))
"""

median = np.median(data)
print("Median")
print(median)

#MEANS ARE SENSETIVE TO OUTLIERS BUT MEDIANS ARE NOT

outlier = np.insert(data,0,5000)
plt.hist(data,label="Data")
plt.axvline(np.mean(data),ls="--",label="Mean Data")
plt.axvline(np.median(data),ls=":",label="Median Data")
plt.axvline(np.mean(outlier),c='r',ls="--",label="Mean Outlier",alpha=0.7)
plt.axvline(np.median(outlier),c='r',ls=":",label="Median Outlier",alpha=0.7)
plt.legend()
plt.xlim(0,20)
plt.show()


#Mode are the most common data in dataset
#If continuous, then bin the data

"""
def get_mode(x):
    values,counts = np.unique(x,return_counts=True)
    max_count_index = np.argmax(counts)
    return values[max_count_index]

print(get_mode[1,7,5,6,3,1,1,2])
"""
mode = st.mode(data)
print(mode)

#get bins for more numbers

hist,edges = np.histogram(data,bins=100)
edge_centers = 0.5 * (edges[1:] + edges[:-1]) #first to last
mode = edge_centers[hist.argmax()]  #get the index of highest value in histogram
#then get bin center for that and that is mode
print(mode)

#if you increase bins amount then mode changes
#to correct above problem - smooth data using scipy in kde

kde = st.gaussian_kde(data)
xvals = np.linspace(data.min(),data.max(),1000)
yval = kde(xvals)
mode = xvals[yval.argmax()]
plt.hist(data,bins=100,density=True,label="Data hist",histtype="step")
plt.plot(xvals,yval,label="KDE")
plt.axvline(mode,label="Mode")
plt.legend()
plt.show()

#with GAUSSIAN Smoothening, now when we change the bin value the kde remains
#same

#TOTAL COMPARISON OF CENTRAL TENDENCY

plt.hist(data,bins=100,label="Data",alpha=0.5)
plt.axvline(mean,label="Mean",ls="--",c='r')
plt.axvline(median,label="Median",ls=":",c='b')
plt.axvline(mode,label="Mode",ls="-",c='g')
plt.legend()
plt.show()
#data is skewed, is the inference
