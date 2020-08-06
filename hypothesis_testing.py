#Hypothesis Testing - ability to ask and quantitatively answer using data(prob.)
#If you formulate two hypothesis how can you identify the true one
#eg: finding whether a player in game has cheated in die roll
#simple QUESTION -> is tommy rolling too many 6?
#How to find out:
#1) Visualise the data
#2) Reduce or quantify the data
#3) Pose our hypothesis(or visualize)
#4) Calculate

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("loaded_500.txt")

unique,counts = np.unique(data,return_counts=True)
print(unique,counts)
plt.hist(data)
plt.show()
#98 times 6s rolled
#plotting done
num_sixes = (data==6).sum()
num_total = data.size

#Pose Hypothesis
#We have two outcomes, if we have a fair die,when we roll it the probability of
#getting 6  = (1/6). As this is discrete with 2 option,we go for binomial dist.

#we also want to know what is the probability of rolling 6 98 times (or more)

from scipy.stats import binom
n = np.arange(num_total)
prob_n = binom.pmf(n,num_total,1/6)
plt.plot(n,prob_n,label="Prob num")
plt.legend()
plt.show()
#now we know there's some problem

prob_n = binom.pmf(n,num_total,1/6)
plt.plot(n,prob_n,label="Prob num")
plt.axvline(num_total/6,ls="--",lw=1,label="Mean num")
plt.axvline(num_sixes,ls=":",color="#ff7272",label="Obs num")
plt.xlabel("Num sizes rolled out of %d rolls".format(num_total))
plt.ylabel("Probability")
plt.legend()
plt.show()
#can't say much from this plot as the observed and mean number are close
#we want the green area under the curve from 98 to 500
#we can do this using survival function OR

d = binom(num_total,1/6)#d is a binomial distribution configured to probability
#and to num_total
plt.plot(n,d.sf(n))
plt.show()


plt.plot(n,d.sf(n))
plt.axvline(num_sixes,ls="--")
sf = d.sf(num_sixes)
plt.axhline(sf,ls="--")
plt.xlabel("num of sixes")
plt.ylabel("Survival function")
plt.show()
print(f"Only {sf * 100:0.1f}% of the time fair die will roll this many or more sixes")
#You would roll more than this many sixes
# CDF <= k ; so SF > k and not >= k
#from this we can see that person is a liar as we can say that 96.3%, his die is
#loaded
