import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,10,200) #200 points distrubuted between -5 and 10
ks = np.arange(50) #from 0-49

#DISCRETE PMF
plt.title("DISCRETE PMF")
pmf_binomial = st.binom.pmf(ks,50,0.25) #0.25 = successful chance, 50 = event
plt.bar(ks,pmf_binomial,label="Binomial Example (Dice)",alpha=0.8)


#Poisson Dist. - change the parameters according to formulae
pmf_poisson = st.poisson.pmf(ks,30) #same as bino because they're discrete
#30 = characteristic rate
plt.bar(ks,pmf_poisson,label="Poisson Example (car crash)",alpha=0.8)
plt.legend()

print("Binomial Dist for chance of rolling 1 10 times")
print(st.binom.pmf(10,50,0.25)) #chances of rolling 10 "1's" on a default
print("Poisson Dist for chance of getting 50 crashes")
print(st.poisson.pmf(50,30)) #what is the chance that we get 50 crashes

plt.show()


#CONTINUOUS PDF/PMF

#Uniform, normal, exponential, student-t, log-normal, skew-normal
plt.title("CONTINUOUS PDF")

pdf_uniform = st.uniform.pdf(x,-4,10)   #parameterized by low and up bound
plt.plot(x,pdf_uniform,label="Uniform (-4,6)")

pdf_normal = st.norm.pdf(x,5,2) #parameterized by location and scalerespectively
plt.plot(x,pdf_normal,label="Normal (5,2)")

pdf_exponential = st.expon.pdf(x,loc=-2,scale=2) #characteristic rate = scale(1)
plt.plot(x,pdf_exponential,label="Exponential(0.5)")

pdf_studentt = st.t.pdf(x,1)# parameterized by degree of freedom
# dof = no of datapoints - 1
plt.plot(x,pdf_studentt,label="Student-t")

pdf_lognorm = st.lognorm.pdf(x,1)#parameterized by scale parameter
plt.plot(x,pdf_lognorm,label="Lognorm(1)")

pdf_skewnorm = st.skewnorm.pdf(x,-6) #default instead of -6 is 0 (alpha param)
plt.plot(x,pdf_skewnorm,label="Skewnorm(-6)")

plt.legend()
plt.xlabel("x")
plt.ylabel("Probability")
plt.show()

# loc and scale(alpha) can be used anywhere as it's mu and sigma. It doesn't
# change anything as it is linear transformation of input vector, eg below
# loc and scale are convinient linear transformation as you can change data
plt.plot(x,st.t.pdf(x,1,loc=4,scale=2),label="In built")
plt.plot(x,st.t.pdf((x-4)/2,1,loc=0,scale=1),label="Manually")

plt.legend()
plt.show()
