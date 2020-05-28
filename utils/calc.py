# 均分321个区间，统计落入格区间的数目
import pandas as pd
import numpy as np

df = pd.read_csv('submit-final.csv', index_col=0)

df['value']=np.log(df['Probability'] / (1 - df['Probability']))

# df.to_csv('final-processed.csv')

min_num = df['value'].min()
max_num = df['value'].max()
N = 101503
divide = 319

bin_list = [0 for i in range(divide + 2)]
bin_list[0] = 0
bin_list[divide + 1] = 0

interval = (max_num - min_num) / divide
for val in df['value'].values:
    bin_list[int((val - min_num)/interval) + 1] += 1

bin_list = np.array(bin_list)

df2 = pd.DataFrame({"count":bin_list})
df2.to_csv("bin.csv")