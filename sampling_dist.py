#sampling fro distribution is great way of testing methods
#common sample form disributions:
#1.Using scipy - from scipy.stats import norm
#scipy can't detect combinational distribution or complete arbitary dist
#2.Rejection sampling - difference in good and bad samples
#when we have distribution from -5 to 5, in rejection sampling most of the
#data is wasted and CPU time is wasted too,so we use inversion sampling
#for empirically derived distribution in 1D, use inversion
#3. Inversion sampling
#you can get cdf by integrating pdf,next invert cdf

#Central Limit Theorem - a distribution of sample means approxs a normal dist
#eg: if you paid 100 people to measure height of 10 people,100 samples of mean
#height values and 100 sample of mean values will have a distribution around it.
