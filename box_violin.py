import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

data1 = np.loadtxt('histogram/example_1.txt')
data2 = np.loadtxt('histogram/example_2.txt')

dataset = pd.DataFrame({
    "value": np.concatenate((data1,data2)),
    "type": np.concatenate((np.ones(data1.shape),np.zeros(data2.shape)))
})

sn.boxplot(x="type",y="value",data=dataset,whis=2.0)
# Box plot is about quartile (recording how data is distributed)
#Distribution in 25%
#effective with swarmplot
sn.swarmplot(x="type",y="value",data=dataset,size=2,color='k',alpha=0.3)
#everyting above and below the box plot is an outlier
#if data is widely distributed then outliers are going to be far away
#BOX PLOT SHRINKS IT TO A CONSTANT AMOUNT OF NUMBER
plt.show()

#Violin plots are better than box plots
sn.violinplot(x="type",y="value",data=dataset)
sn.swarmplot(x="type",y="value",data=dataset,size=2,color='k',alpha=0.3)
plt.show()

sn.violinplot(x="type",y="value",data=dataset,inner="quartile",bw=0.2)
#scipy calculates the bandwidth(broadness)
#we can also divide it into 2 halves check the violin documentation
#https://seaborn.pydata.org/generated/seaborn.violinplot.html
