import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('height_weight.csv',usecols=['height','weight'])

#Co-Variance - Checking variance of one column with respect to another
#It has both variance and correlation combined into 1 matrix
#           (       a,a         a,b  )
#          (    Var         Var       )
#   Cov = (                            )
#          (       b,a         b,b    )
#           (   Var         Var     )
print(data.head())
print()

"""
print("Incorrect covariance")
covariance = np.cov(data)
print(covariance) #this expects each row and column to be a different variable
"""
print()
print()
#correct it by transposing or rowvar=False
covariance = np.cov(data.T) # or covariance = np.cov(data,rowvar=False)
print("Covariance")
print(covariance)
print()
print()
print("Covariance")
covariance_pandas = data.cov()
print(covariance_pandas)
print()
print()


#CORRELATION formula
#https://www.thoughtco.com/how-to-calculate-the-correlation-coefficient-3126228
#np.corrcoef or pd.DataFrame.corr
#Value of correlation goes from -1 to 1
# 1 = one variable goes up other does too
# -1 = One variable going up and other going down

corref = np.corrcoef(data.T)
print("Correlation")
print(corref)
print()
print("Pandas Correlation")
print()
print(data.corr())
# If variable can be derived from one another they are correlated
