import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('height_weight.csv')
print(df.info())
print(df.describe())

hist, x_edge, y_edge = np.histogram2d(df["height"],df["weight"],bins=20)
x_centre = 0.5 * (x_edge[1:] + x_edge[:-1]) #0.5 to take the half
y_centre = 0.5 * (y_edge[1:] + y_edge[:-1])
#data is noisy

plt.contour(x_centre,y_centre,hist)     #you can add levels to this to magnify
plt.xlabel("Height")
plt.ylabel("Weight")
