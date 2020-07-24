#sampling fro distribution is great way of testing methods
#common sample form disributions:
#1.Using scipy - from scipy.stats import norm
#scipy can't detect combinational distribution or complete arbitary dist
#2.Rejection sampling - difference in good and bad samples
#when we have distribution from -5 to 5, in rejection sampling most of the
#data is wasted and CPU time is wasted too,so we use inversion sampling
#for empirically derived distribution in 1D, use inversion
#3. Inversion sampling
#you can get cdf by integrating pdf,next invert cdf

#Central Limit Theorem - a distribution of sample means approxs a normal dist
#eg: if you paid 100 people to measure height of 10 people,100 samples of mean
#height values and 100 sample of mean values will have a distribution around it.

#using scipy - rvs is only required (random value sample)

from scipy.stats import norm,uniform
from scipy.integrate import simps
import numpy as np
import matplotlib.pyplot as plt

plt.title("Sampling")
plt.hist(norm.rvs(loc=10,scale=2,size=1000))#loc=mean,size=sample of 1000,wdth=2
plt.show()


#for rolling 3 die

sample= np.ceil(uniform.rvs(loc=0,scale=6,size=(1000,3))).sum(axis=1)#size of 2D
#in 1D, therefore 1000 samples
#print(sample)

plt.hist(sample)
plt.show()

#Rejection sampling:
#1) Uniformly sample x value
#2) Generate uniform y value from 0 to max probability in PDF
#3) If y>p(x), then throw the point


#eg: p(x) = sin(x^2)+1 from 0->4

def pdf(x):
  return np.sin(x**2)+1

xs = np.linspace(0,4,200)
ps= pdf(xs)
plt.title("Rejection Sampling")
plt.plot(xs,ps)
plt.fill_between(xs,0,ps,alpha=0.1)
plt.xlim(0,4)
plt.ylim(0,2)
plt.show()
#low value around dips and high number of values around peak

n = 100 #(samples)
random_x = uniform.rvs(loc=0,scale=4,size=n)
random_y = uniform.rvs(loc=0,scale=2,size=n)

plt.scatter(random_x,random_y)
plt.plot(xs,ps,c="g")
plt.fill_between(xs,0,ps,color="b",alpha=0.1)
plt.xlim(0,4),plt.ylim(0,2)
plt.show()
#blue points are proposal points
#to find the position whether they're above green line or not ->
passed = random_y <= pdf(random_x)
plt.scatter(random_x[passed],random_y[passed])
#this passes the points that did not pass the curve
plt.scatter(random_x[~passed],random_y[~passed],marker='x',s=30,alpha=0.5)
plt.plot(xs,ps,c="r")
plt.fill_between(xs,0,ps,color="b",alpha=0.1)#psuedo probability function
plt.xlim(0,4),plt.ylim(0,2)
plt.show()

from scipy.integrate import simps
n2=100000
x_test = uniform.rvs(scale=4,size=n2)
x_final = x_test[uniform.rvs(scale=2,size=n2) <= pdf(x_test)]
print()
print(len(x_final))
print()
plt.hist(x_final,density=True,histtype="step",label="Sample Distribution")
plt.plot(xs, ps / simps(ps,x=xs),c="b",marker="x",label = "Empirical Dist")
plt.legend(loc=2)
plt.show()
#not actual pdf as it is divided by simps



#INVERSION SAMPLING
#How to -> start with PDF, turn it into CDF, invert the CDF,uniformly sample 0-1
#trace it back to x
#eg: if p(x) = 3x^2 from 0->1
#                                            x
#To convert PDF -> CDF, integrate, eg: CDF = |p(x)dx = x^3
#                                            0
#Then invert it, eg: x^3 = y; y^3 = x
#y = x^1/3, therefore, x = CDF^1/3

#code
def pdf(x):
  return 3*x **2

def cdf(x):
  return x**3

def icdf(cdf):
  return cdf**(1/3)


xs = np.linspace(0,1,100)
pdfs = pdf(xs)
cdfs = cdf(xs)

n=2000
u_samps = uniform.rvs(size=n)
x_samps = icdf(u_samps)

fig,axes = plt.subplots(ncols=2,figsize=(10,4))

axes[0].plot(xs,pdfs,color="b",label="PDF")
axes[0].hist(x_samps,density="True",histtype="step",label="Sample Dist")

axes[1].plot(xs,cdfs,color="g",label="CDF")
axes[1].hlines(u_samps,0,x_samps,linewidth=0.1,alpha=0.3)
axes[1].vlines(x_samps,0,u_samps,linewidth=0.1,alpha=0.3)

axes[0].legend()
axes[1].legend()

axes[0].set_xlim(0,1)
axes[0].set_ylim(0,3)

axes[1].set_xlim(0,1)
axes[1].set_ylim(0,1)

plt.show()


#using the same function on previous PDF
#this might not always run as it does not come under the given range,
#so keep ruunning until you get lucky :D  :)
from scipy.interpolate import interp1d

def pdf(x):
  return np.sin(x**2)+1

xs = np.linspace(0,4,10000)
pdfs = pdf(xs)
cdfs = pdfs.cumsum() / pdfs.sum() #dangerous because it will never be 0
#code has potential to break as 1st term is 1/10000

u_samps = uniform.rvs(size=4000)
x_samps = interp1d(cdfs,xs)(u_samps)


fig,axes = plt.subplots(ncols=2,figsize=(10,4))

axes[0].plot(xs,pdfs/4.747,color="b",label="Analytic PDF")#pdf/4.747=normalizing
axes[0].hist(x_samps,density="True",histtype="step",label="Sample Dist")
axes[0].legend(loc=3), axes[0].set_xlim(0,4)

axes[1].plot(xs,cdfs,color="g",label="Analytic CDF")
axes[1].hlines(u_samps,0,x_samps,linewidth=0.1,alpha=0.3)
axes[1].vlines(x_samps,0,u_samps,linewidth=0.1,alpha=0.3)
axes[1].legend(loc=2)

axes[1].set_xlim(0,4)
axes[1].set_ylim(0,1)

plt.show()
