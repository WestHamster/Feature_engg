import pandas as pd
import numpy as np

filename = ('data_preparation/Diabetes.csv')

df = pd.read_csv(filename)
print(df.info(),"\n\n")
print(df.head(),"\n\n")

#rows with 0 can be replaced with NaN
# if null values --> df.fillna(0)
# to drop na --> df.dropna()
#first decide which columns to use in the dataset
df1 = df[["Glucose","BMI","Age","Outcome"]]
print(df1.head(),"\n\n")
print(df1.describe(),"\n\n")

# get rid of 0's -> 1. check the columns excluding the outcomes/prediction val
#2. drop the whole row with 0 value
df2 = df1.loc[~(df1[df1.columns[:-1]]==0).any(axis=1)]
#make all the values with 0 (true) to drop
print(df2.info(),"\n\n")

print(df2.groupby("Outcome").mean(),"\n\n")
#implementing different aggregate method for different groups
print(df2.groupby("Outcome").agg({"Glucose":"mean","BMI":"median","Age":"sum"}),"\n\n")
#To find out how skewed data is and what are the outliers
print(df2.groupby("Outcome").agg(["mean","median"]),"\n\n")
