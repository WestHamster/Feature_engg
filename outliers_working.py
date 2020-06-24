import numpy as np
import matplotlib.pyplot as plt


data1 = np.loadtxt('outliers/outlier_1d.txt')
data2 = np.loadtxt('outliers/outlier_2d.txt')
data3 = np.loadtxt('outliers/outlier_curve.txt')

print(data1.shape,data2.shape,"\n\n")


# How to prune outliers on data distribution:
#1. Model your data as analytic distribution
#2. Find all points below a certain probability (eg:z-score)
#3. Remove them
#4. Refit the distribution, and run again from step 1

mean, std = np.mean(data1), np.std(data1)
z_score = np.abs((data1 - mean)/std)
threshold = 3
good = z_score < threshold

print(f"Rejecting {(~good).sum()} points\n\n")
visual_scatter = np.random.normal(size=data1.size)
plt.scatter(data1[good],visual_scatter[good],s=2,label="Good",color="#4CAF50")
plt.scatter(data1[~good],visual_scatter[~good],s=2,label="Bad",color="#F44336")
plt.legend()
plt.show()
