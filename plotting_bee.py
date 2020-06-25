import pandas as pd
import numpy as np
import seaborn as sn

data1 = np.loadtxt('histogram/example_1.txt')
data2 = np.loadtxt('histogram/example_2.txt')

dataset = pd.DataFrame({
    "value": np.concatenate((data1,data2)),
    "type": np.concatenate((np.ones(data1.shape),np.zeros(data2.shape)))
})

print(dataset.info)

sn.swarmplot(dataset["value"])
plt.show()
#datapoint from both data1 and data2
#improve by seperating data1 and data2

sn.swarmplot(x="type",y="value",data=dataset,size=2)
#both data show strong peak but no bimodal distribution
plt.show()
#bee swarm plot becomes more effective as we have more categories
#effective in sales sheet but lack scientific rigor for papers 
