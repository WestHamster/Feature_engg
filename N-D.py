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


#Scatter matrix
pd.plotting.scatter_matrix(df_copy,figsize=(7,7))

df2 = df_copy.dropna()
colors = df2["Outcome"].map(lambda x:"#44d9ff" if x else "#f95b4a")
pd.plotting.scatter_matrix(df2,figsize=(7,7),color=colors)
