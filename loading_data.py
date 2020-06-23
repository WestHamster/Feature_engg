import numpy as np
import pandas as pd
import pickle

filename = "loading_data/load.csv"

# Loading file using simple editors
cols = None
data = []

with open(filename) as f:
    for line in f.readlines():
        vals = line.replace("\n","").split(",")
        print(vals)
        if cols is None:
            cols = vals
        else:
            data.append([float(x) for x in vals])

df = pd.DataFrame(data,columns=cols)
print("\n",df.dtypes)
print(df.head(),"\n\n")

#loading file using numpy

df1 = np.loadtxt(filename,skiprows=1,delimiter=",")
print("\n",df1.dtype)
print(df1[:5,:],"\n\n")
#output is 2D array not dataframe

#loading file using genfromtext

df2 = np.genfromtxt(filename,delimiter=",",dtype=None,names=True)
print(df2.dtype)
print(df2[:5],"\n\n")


#loading file using pandas
df3 = pd.read_csv(filename)
print(df3.dtypes)
print(df3.head(),"\n\n")


#loading file from pickle
#binary file
with open('loading_data/load_pickle.pickle',"rb") as f:
    df4 = pickle.load(f)
print(df4.dtypes)
print(df4.head())
