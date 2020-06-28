import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from chainconsumer import ChainConsumer

df = pd.read_csv('height_weight.csv')
print(df.info())
print(df.describe())

m = df["sex"] == 1
plt.scatter(df.loc[m,"height"], df.loc[m,"weight"], c="#16c6f7",s=1,label="Male")
plt.scatter(df.loc[~m,"height"], df.loc[~m,"weight"], c="#ff8b87",s=1,label="Female")

plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend(loc=2)
#blue is male as we can see from the height distribution
#read chain consumer for probability to analyse them
"""
#Advanced version of probability

params = ["height","weight"]
male = df.loc[m,params].values
female = df.loc[~m,params].values

print(male.shape,female.shape)

c = ChainConsumer()
c.add_chain(male,parameters=params,name="Male",kde=1.0,color="b")
c.add_chain(female,parameters=params,name="Female",kde=1.0,color="r")
c.configure(contour_labels="confidence")
c.plotter.plot(figsize=2.0)
c.plotter.plot_summary(figsize=2.0) #testing multiple models on the data
"""

#NEVER USE  PIE CHARTS
