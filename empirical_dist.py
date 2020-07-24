import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.integrate import simps

xs = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,
    5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
ys = [0.2,0.165,0.167,0.166,0.154,0.134,0.117,0.108,0.092,0.06,0.031,0.028,
    0.048,0.077,0.103,0.119,0.119,0.103,0.074,0.038,0.003]

plt.scatter(xs,ys)
plt.xlabel("x")
plt.ylabel("Observed PDF")
plt.show()
#This is a continuous distribution

#span x from min to max with these data points
#interpolating the data
x = np.linspace(min(xs),max(xs),1000)
y1 = interp1d(xs,ys)(x)
#interpolating xs and ys to x line

plt.scatter(xs,ys,s=30,label="Data",c="b")
plt.plot(x,y1,label="Linear(default)")
plt.legend()
plt.show()
#linear interpolating in our data
#but if we have sparse data then it is not shown correctly
#depends on data

#another type of interpolation - nearest
x = np.linspace(min(xs),max(xs),1000)
y2 = interp1d(xs,ys,kind="nearest")(x)
#works as a step function in the graph shown below
#useful for discrete function but not very useful for
#smooth changing values

plt.scatter(xs,ys,s=30,label="Data",c="b")
plt.plot(x,y1,label="Linear(default)")
plt.plot(x,y2,label="Nearest")
plt.legend()
plt.show()

#another type of interpolation - quadratic
x = np.linspace(min(xs),max(xs),1000)
y3 = interp1d(xs,ys,kind="quadratic")(x)
#works as a step function in the graph shown below
#useful for discrete function but not very useful for
#smooth changing values

plt.scatter(xs,ys,s=30,label="Data",c="b")
plt.plot(x,y1,label="Linear(default)")
plt.plot(x,y2,label="Nearest",alpha=0.3)
plt.plot(x,y3,label="Quadratic",ls="-")
plt.legend()
plt.show()
#on the changing gradient you can see the difference
#between the nearest and quadratic


#another type of interpolation - cubic
x = np.linspace(min(xs),max(xs),1000)
y4 = interp1d(xs,ys,kind="cubic")(x)

plt.scatter(xs,ys,s=30,label="Data",c="b")
plt.plot(x,y1,label="Linear(default)")
plt.plot(x,y2,label="Nearest",alpha=0.3)
plt.plot(x,y3,label="Quadratic",ls="-")
plt.plot(x,y4,label="Cubic",ls="-")
plt.legend()
plt.show()
#the more complex interpolation,the slower
#it's(difference in quadratic and cubic) going to be

from scipy.interpolate import splev,splrep

#another type of interpolation - splev
x = np.linspace(min(xs),max(xs),1000)
y5 = splev(x,splrep(xs,ys))
#if data changing quickly, using cubic spline

plt.scatter(xs,ys,s=30,label="Data",c="b")
plt.plot(x,y1,label="Linear(default)")
plt.plot(x,y2,label="Nearest",alpha=0.3)
plt.plot(x,y3,label="Quadratic",ls="-")
plt.plot(x,y4,label="Cubic",ls="-")
plt.plot(x,y5,label="Spline",ls="-",alpha=0.5,c="#0000")
plt.legend()
plt.show()

#the red changes colour as both quadratic and spline are same


#Using the interp1d we can find the probability for any x value
#Using scipy.integrate we can calculate the CDF and probability in two bounds

#scipy.integrate.trapz = low accuracy but high speed - accuracy scales as O(h)
#scipy.integrate.simps = med accuracy but very high speed - acc scales as O(h^2)
#scipy.integrate.quad = high accuracy but low speed - arbitary accuracy


def get_prob(xs,ys,a,b): #add another variable here resolution=1000
  #a,b = bounds
  #to normalize, use the below
  x_norm = np.linspace(min(xs),max(xs),1000) #add resolution here instead of no
  y_norm = interp1d(xs,ys,kind="quadratic")(x_norm)
  normalisation = simps(y_norm,x=x_norm)
  x_vals = np.linspace(a,b,1000)#add resolution here instead of number
  y_vals = interp1d(xs,ys,kind="quadratic")(x_vals) #general solution
  #could be tweaked to gain more accuracy
  return simps(y_vals,x=x_vals)/normalisation

def get_cdf(xs,ys,v):#value of cdf at
  return get_prob(xs,ys,min(xs),v) #if xs is np array -> xs.min(),upto value v

def get_sf(xs,ys,v):
  return 1 - get_cdf(xs,ys,v)#definition of the survival function
  #OR return get_prob(xs,ys,v,max(xs))

print(get_prob(xs,ys,0,10)) #simps has some issue & needs to be normalized,
#check the normalized code above and check without normalized
#another problem is of numbers added to np.linspace,try changing
#x_vals = np.linspace(a,b,100), to solve this
#add a variable to it, use of resolution can solve the problem


v1,v2 = 6,9.3
area = get_prob(xs,ys,v1,v2)

plt.scatter(xs,ys,s=30,label="Data",color="w")
plt.plot(x,y3,linestyle="-",label="Interpolation")
plt.fill_between(x,0,y3,where=(x>=v1)&(x<=v2),alpha=0.2) #fill in the values
plt.annotate(f"p = {area}.3f",(7,0.05))
plt.legend()
plt.show()


#comparing cdf
x_new = np.linspace(min(xs),max(xs),100)
cdf_new = [get_cdf(xs,ys,i) for i in x_new] #expensive way of cdf_new

cheap_cdf =y3.cumsum()/y3.sum()
plt.plot(x_new,cdf_new,label="Interpolated CDF",c="r")
plt.plot(x,cheap_cdf,label="Super cheap CDF for specific cases",c="g")
plt.ylabel("CDF")
plt.xlabel("x")
plt.legend()
plt.show()
#for smooth data you can use the cheap cdf method
#you can see the interpolated and the cheap cdf coming together
