# 算分数
import numpy as np
import pandas as pd

def get_score(p):
    score = 600 - 81.8*np.log(p/(1-p))
    score = np.maximum(score, 300)
    score = np.minimum(score, 900)
    return score

df = pd.read_csv('submit-final.csv')
df['Score'] = get_score(df['Probability'].values)

df.to_csv('scores.csv')