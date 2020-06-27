import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('height_weight.csv')
print(df.info())
print(df.describe())

#kernel density estimation
#kernel is specifying  how data is smoothened. Here Gaussian is used
#violin plot also uses gaussian
sb.kdeplot(df["height"],df["weight"],cmap="viridis",bw=(2,20))
#jaggerness tells there are data points in it
#(2,20) -> here 20 is the gaussian width
plt.hist2d(df["height"],df["weight"],bins=20,cmap="magma",alpha=0.3)
#convolving 2D Histogram with kde
plt.show()
sn.kdeplot(df["height"],df["weight"],cmap="magma",shade=True)
#plot of probability surface
