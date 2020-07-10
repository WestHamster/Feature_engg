import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

data = np.loadtxt("dataset.txt")
"""
def get_variance(x):
    mean = np.mean(x)
    sum = 0
    for i in x:
        sum += (i-mean)**2
    return sum / (len(x)-1)

print(get_variance([1,2,5,3,4,5,2,4]))
"""

variance = np.var(data,ddof=1)  #ddof = delta degree of freedom
print("Variance")
print(variance)
print()
print()
#STANDARD DEVIATION - square root of variance

std = np.std(data)
print("Standard dev\t\t Variance")
print(std,"\t",std**2)
print()
print()

#GAUSSIAN APPROXIMATION

xs = np.linspace(data.min(),data.max(),100)
ys = st.norm.pdf(xs,loc=np.mean(data),scale=std)

plt.hist(data,bins=50,density=True,histtype="step",label="Data")
plt.plot(xs,ys,label="Normal approximation")
plt.legend()
plt.ylabel("Probability")
plt.show()
print()
print()
#With variance and std we can recontruct the data almost


#Skewness - 3rd Moment
#1st - zero, 2nd - Variance, 3rd - Skewness
#cubic distance from mean
"""
def get_skew(xs):
    mean = np.mean(xs)
    var = np.var(xs)
    sum = 0
    for x in xs:
        sum += (x-mean)**3
    return (sum / (len(xs))) / (var ** 1.5)
print(get_skew([1,10,4,3]))
"""

skewness = st.skew(data)
print("Skewness")
print(skewness)

#update Gaussian approximation to include skewness
xs = np.linspace(data.min(),data.max(),100)
ys = st.norm.pdf(xs,loc=np.mean(data),scale=std)
ys1 = st.skewnorm.pdf(xs,skewness,loc=np.mean(data),scale=std)
plt.hist(data,bins=50,density=True,histtype="step",label="Data")
plt.plot(xs,ys,label="Normal approximation")
plt.plot(xs,ys1,label="Skewnormal approximation")
plt.legend()
plt.ylabel("Probability")
plt.show()
print()
print()

#not a good approx because mean is changed, so change and fit the data

xs = np.linspace(data.min(),data.max(),100)
ys = st.norm.pdf(xs,loc=np.mean(data),scale=std)
ps = st.skewnorm.fit(data) #fitting the data (mean and std dev. by scipy)
ys1 = st.skewnorm.pdf(xs,*ps) #passing the fitted data

plt.hist(data,bins=50,density=True,histtype="step",label="Data")
plt.plot(xs,ys,label="Normal approximation")
plt.plot(xs,ys1,label="Skewnormal approximation")
plt.legend()
plt.ylabel("Probability")
plt.show()
print()
print()


#KURTOSIS - same to skewness just the difference of mean to 4th power
"""
def get_k(xs):
    mean = np.mean(xs)
    var = np.var(xs)
    sum = 0
    for x in xs:
        sum += (x-mean)**4
    return (sum / (len(xs))) / (var ** 2)
print(get_k([1,10,4,3]))
"""

kurtosis = st.kurtosis(data,fisher=False)
print("Kurtosis")
print(kurtosis)
print()
print()
#you won't get same results here from the function and st.kurtosis(), you have
#to pass fisher=False which is normalisation of kurtosis

#Problem while approximation is that data is Bi-Modal distribution and no
#moment will take this into account


#PERCENTILE

ps = np.linspace(0,100,10)
x_per = np.percentile(data,ps)

xs = np.sort(data)
ys = np.linspace(0 ,1 ,len(data))

plt.plot(xs, ys * 100, label="ECDF")
plt.plot(x_per,ps,label="Percentile",marker=".",ms=10)
plt.legend()
plt.ylabel("Percentile")
plt.show()
# Green - Emperical CDF
# Yellow - 10 percentile for numpy to calculate
# Difference in tails in curve because the data is linearly sampled.
# Data seems to be Gaussian because of it's tails.
# Loss of data at tails can be seen
ps = 100 * st.norm.cdf(np.linspace(-3,3,30))
x_per = np.percentile(data,ps)

xs = np.sort(data)
ys = np.linspace(0 ,1 ,len(data))

plt.plot(xs, ys * 100, label="ECDF")
plt.plot(x_per,ps,label="Percentile",marker=".",ms=10)
plt.legend()
plt.ylabel("Percentile")
plt.show()
#not much effort wasted at the tail part but to take tail to account,
#add an insert value to ps
ps = 100 * st.norm.cdf(np.linspace(-3,3,30))
ps = np.insert(ps,0,0)
ps = np.insert(ps,-1,100)
x_per = np.percentile(data,ps)

xs = np.sort(data)
ys = np.linspace(0 ,1 ,len(data))

plt.plot(xs, ys * 100, label="ECDF")
plt.plot(x_per,ps,label="Percentile",marker=".",ms=10)
plt.legend()
plt.ylabel("Percentile")
plt.show()
#Tails covered in percentile
