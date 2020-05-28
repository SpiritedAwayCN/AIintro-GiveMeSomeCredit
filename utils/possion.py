# 生成泊松分布表

import numpy as np
import pandas as pd
import math

val_lambda = 27
exp_lambda = math.exp(-val_lambda)

p = [0 for i in range(321)]
p[0] = exp_lambda
for i in range(1, 321):
    p[i] = p[i-1] * val_lambda / i

pd.DataFrame({"Possion":p}).to_csv('possion.csv')