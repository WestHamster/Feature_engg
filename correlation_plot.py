import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('data_preparation/Diabetes.csv')
print(df.head(),"\n\n")

cols = [c for c in df.columns if c not in ["Pregnancies","Outcome"]]
df_copy = df.copy()
df_copy[cols] = df_copy[cols].replace({0: np.NaN})
print(df_copy.head(),"\n\n")
print(df_copy.info())

print(df_copy.corr())

sn.heatmap(df_copy.corr())
plt.show()

sn.heatmap(df_copy.corr(),annot=True,cmap="viridis",fmt="0.2f")
plt.show()
