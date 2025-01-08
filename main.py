import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('QueryResults.csv',names= ['DATE','TAG','POSTS'])
df.head()
reshape = df.pivot(index='DATE',columns='TAG',values='POSTS')
reshape.head()
reshape=reshape.fillna(0)
reshape.head()
roll_df=reshape.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=16)
plt.savefig('my_plot.png')


