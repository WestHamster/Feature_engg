#Central Limit Theorem states that dist. of sample mean is normally dist.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon,skewnorm

def get_data(n):
    data = np.concatenate((expon.rvs(scale=1,size=n//2),skewnorm.rvs(5,loc=3,size=n//2)))
    #getting exp dist data
    #now shuffle the data
    np.random.shuffle(data)
    return data

plt.hist(get_data(2000))    #not a gaussian,normal dist
plt.show()

d10 = get_data(10)
print(d10.mean())   #gives mean of 10 random numbers

means = [get_data(10).mean() for i in range(10000)]
plt.hist(means)
plt.show()
print("Std. Dev.=",np.std(means))

means = [get_data(100).mean() for i in range(10000)]
plt.hist(means)
plt.show()  #this gives better result than before
print("Std. Dev. for 100 data point mean=",np.std(means))

num_sample = [10,50,100,500,1000,5000,10000]
stds=[]
for n in num_sample:
    stds.append(np.std([get_data(n).mean() for i in range(1000)]))
plt.plot(num_sample,stds,'o',label='Obs Scatter')
plt.plot(num_sample,1/np.sqrt(num_sample),label='Random function',alpha=0.5)
#standard deviation is related to inverse number of samples
plt.legend()
plt.show()

plt.hist([get_data(100).mean() for i in range(100)])
plt.show()
#by changing the range to power of 10, you can observe that it reaches normal dist.
#width depends on samples went into number(10,100,1000)

n = 1000
data = get_data(n)
sample_mean = np.mean(data)
uncertainity_mean = np.std(data)/np.sqrt(n)
print(f"We have determined the mean of population to be {sample_mean:0.2f} +- {uncertainity_mean:.2f}")
#1 sigma = 1 standard deviation away from mean, represented by +-

from scipy.stats import norm

xs = np.linspace(sample_mean -0.2,sample_mean+0.2,100)
ys = norm.pdf(xs,sample_mean,uncertainity_mean)
plt.plot(xs,ys)
plt.xlabel("population mean")
plt.ylabel("Probability")
plt.show()
#normal distribution is always formed when sample size increases
#using CLT, to provide uncertainity, is the most way it's used
