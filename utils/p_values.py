# 卡方检验，计算V

import numpy as np
import pandas as pd

data = pd.read_csv("bin.csv", index_col=0)

n = 321

def get_p_val(P, X):
    P[P==0] = 1e-12
    return np.sum(((X-P)**2)*(n/P))


print("Possion", get_p_val(data['p'].values, data['Possion'].values))
print("Maxwell", get_p_val(data['p'].values, data['Maxwell'].values))
print("Chi2-38", get_p_val(data['p'].values, data['Chi^2-38'].values))
print("Maxwell2", get_p_val(data['p'].values, data['Maxwell2'].values))