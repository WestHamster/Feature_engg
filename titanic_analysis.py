import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.graph_objects as go

df = pd.read_csv('titanic/train.csv',index_col=0)
print(df.head())
print()
print(df.describe(),"\n")
print(df.columns,"\n")
print("Columns      Empty\n")
print(df.isnull().any())

def survived(input):
    sn.set(style="whitegrid")
    sn.countplot(input["Survived"])
    plt.show()
survived(df)
print()
print(str(round(np.mean(df['Survived']) * 100)) + "% of the passengers on the RMS Titanic survived.\n")
print(str(round((sum((df[df['Sex'] == 'female'])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were female.")
print(str(round((sum((df[df['Sex'] == 'male'])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were male.\n")
print(str(round((sum((df[df['Pclass'] == 1])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were first class.")
print(str(round((sum((df[df['Pclass'] == 2])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were second class.")
print(str(round((sum((df[df['Pclass'] == 3])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were third class.\n")
print(str(round((sum((df[df['Age'] <= 20])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were 20 or younger.")
print(str(round((sum((df[(df['Age'] > 20) & (df['Age'] < 50)])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were between 20 and 50.")
print(str(round((sum((df[df['Age'] >= 50])['Survived']) / sum(df['Survived'])) * 100)) + "% of the survivors were 50 or older.\n")


survivors = df[df['Survived'] == 1]
female_survivors = df[df['Sex'] == 'female']
male_survivors = df[df['Sex'] == 'male']
classes = ['First Class', 'Second Class', 'Third Class']
female_classes = female_survivors['Pclass'].value_counts(sort=False, normalize=True).to_list()
male_classes = male_survivors['Pclass'].value_counts(sort=False, normalize=True).to_list()
fig = go.Figure(data=[
    go.Bar(name='Female', x=classes, y=female_classes),
    go.Bar(name='Male', x=classes, y=male_classes)])
fig.update_layout(barmode='stack', width=400, height=400, title="Class and Sex of Survivors Ratios")
fig.show()
