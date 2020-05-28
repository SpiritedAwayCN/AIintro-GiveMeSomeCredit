# 统计落入各区间的分数个数
import numpy as np
import pandas as pd

df = pd.read_csv('scores.csv')

div = 50
interval = (900 - 300) // div
mylist = [0 for i in range(div)]

for v in df['Score'].values:
    mylist[int(v - 300) // interval] += 1

pd.DataFrame({'count':mylist}).to_csv("score_bin.csv")