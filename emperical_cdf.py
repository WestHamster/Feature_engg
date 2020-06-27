import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

#Emperical CDF
#the more bins == the more noise
data1 = np.loadtxt('empirical_cdf/example_1.txt')
data2 = np.loadtxt('empirical_cdf/example_2.txt')


sd1 = np.sort(data1)
sd2 = np.sort(data2)
cdf = np.linspace(1/data1.size,1,data1.size) #because data1.size == data2.size
#1/data1.size how well quarantile supports our data
plt.plot(sd1,cdf,label="Data1 CDF")
plt.plot(sd2,cdf,label="Data2 CDF")
plt.hist(data1,histtype="step",density=True,alpha=0.3)
plt.hist(data2,histtype="step",density=True,alpha=0.3)
plt.legend()
