import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

data1 = np.loadtxt('example_1.txt')
data2 = np.loadtxt('example_2.txt')

print(data1.shape," ",data2.shape)

#Histogram plots

bins = np.linspace(min(data1.min(),data2.min()),max(data1.max(),data2.max()),50)
#plt.hist(data1,label="data1")
counts1, bins, _ = plt.hist(data1,bins=bins,label= "Data1")
plt.hist(data2,bins = bins,label="data2")
plt.legend()
plt.ylabel("Counts");
plt.show()

bins = np.linspace(min(data1.min(),data2.min()),max(data1.max(),data2.max()),50)
#plt.hist(data1,label="data1")
counts1, bins, _ = plt.hist(data1,bins=bins,label= "Data1",density=True)
plt.hist(data2,bins = bins,label="data2",density=True)
plt.legend()
plt.ylabel("probability");
plt.show()

#improving visuals

bins = np.linspace(min(data1.min(),data2.min()),max(data1.max(),data2.max()),50)
#plt.hist(data1,label="data1")
counts1, bins, _ = plt.hist(data1,bins=bins,label= "Data1",density=True,histtype="step",lw=1)
plt.hist(data2,bins = bins,label="data2",density=True,histtype="step",ls=":")
plt.legend()
plt.ylabel("probability");
plt.show()

#stacked plot

bins = np.linspace(min(data1.min(),data2.min()),max(data1.max(),data2.max()),50)
#plt.hist(data1,label="data1")
plt.hist([data1,data2],bins=bins,label= "Stacked",density=True,histtype="barstacked",alpha=0.5)

plt.hist(data1,bins=bins,label= "Data1",density=True,histtype="step",lw=1)
plt.hist(data2,bins = bins,label="data2",density=True,histtype="step",ls=":")
plt.legend()
plt.ylabel("probability");
plt.show()

#If you have multiple hist plots don't go for bins

bins=10
plt.hist([data1,data2],bins=bins,label= "Stacked",density=True,histtype="barstacked",alpha=0.5)

plt.hist(data1,bins=bins,label= "Data1",density=True, histtype="step",lw=1)
plt.hist(data2,bins = bins,label="data2",density=True, histtype="step",ls=":")
plt.legend()
plt.ylabel("probability");
plt.show()
