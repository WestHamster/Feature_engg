import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('height_weight.csv')
print(df.info())
print(df.describe())

plt.hist2d(df["height"],df["weight"],bins=20,cmap="magma")
plt.xlabel("Height")
plt.ylabel("Weight")
#positive correlation in height and weight
