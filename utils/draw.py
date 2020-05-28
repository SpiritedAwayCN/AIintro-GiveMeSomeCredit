# 画图

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as trs
import math
import seaborn

data = pd.read_csv('cs-training.csv', index_col=0)
data.drop_duplicates(inplace=True)

data.boxplot(column=['NumberOfTime30-59DaysPastDueNotWorse',
                     'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfTimes90DaysLate'])
plt.title('Before Cleaning', fontproperties='Times New Roman', size=16)
plt.xticks([1, 2, 3], ['30-59Days', '60-89Days', '90Days'],
           fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('001_NumberOfTime_before_cleaning.png', dpi=1200)
plt.close()

data = data[(data['NumberOfTime30-59DaysPastDueNotWorse'] < 80) &
            (data['NumberOfTime60-89DaysPastDueNotWorse'] < 80) & (data['NumberOfTimes90DaysLate'] < 80)]

data.boxplot(column=['NumberOfTime30-59DaysPastDueNotWorse',
                     'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfTimes90DaysLate'])
plt.title('After Cleaning', fontproperties='Times New Roman', size=16)
plt.xticks([1, 2, 3], ['30-59Days', '60-89Days', '90Days'],
           fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('002_NumberOfTime_after_cleaning.png', dpi=1200)
plt.close()

data.boxplot(column='age', figsize=(5, 5))
plt.title('Age', fontproperties='Times New Roman', size=16)
plt.xticks(fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('003_Age_box.png', dpi=1200)
plt.close()

data = data[data['age'] != 0]
data.hist(column='age', bins=data['age'].max()-data['age'].min())
plt.title('Age', fontproperties='Times New Roman', size=16)
plt.xticks(fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('004_Age_hist.png', dpi=1200)
plt.close()

data['LogDebtRatio'] = data['DebtRatio'].apply(
    lambda x: math.log(x) if x else np.nan)
plt.subplots(figsize=(8, 5))
plt.subplot(121)
data.boxplot(column='DebtRatio')
plt.xticks([1], ['Original'], fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.subplot(122)
data.boxplot(column='LogDebtRatio')
plt.xticks([1], ['Logarithmic'], fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.suptitle('Before and After Logarithmic Comparison\n(DebtRatio)',
             fontproperties='Times New Roman', size=16)
plt.savefig('005_DebtRatio_box_Logarithmic_Comparison.png', dpi=1200)
plt.close()

data['LogRevolvingUtilizationOfUnsecuredLines'] = data['RevolvingUtilizationOfUnsecuredLines'].apply(
    lambda x: math.log(x) if x else np.nan)
plt.subplots(figsize=(8, 5))
plt.subplot(121)
data.boxplot(column='RevolvingUtilizationOfUnsecuredLines')
plt.xticks([1], ['Original'], fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.subplot(122)
data.boxplot(column='LogRevolvingUtilizationOfUnsecuredLines')
plt.xticks([1], ['Logarithmic'], fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.suptitle('Before and After Logarithmic Comparison\n(RevolvingUtilizationOfUnsecuredLines)',
             fontproperties='Times New Roman', size=16)
plt.savefig('006_RUOUL_box_Logarithmic_Comparison.png', dpi=1200)
plt.close()

data['LogMonthlyIncome'] = data['MonthlyIncome'].apply(
    lambda x: math.log(x) if x else np.nan)
plt.subplots(figsize=(8, 5))
plt.subplot(121)
data.boxplot(column='MonthlyIncome')
plt.xticks([1], ['Original'], fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.subplot(122)
data.boxplot(column='LogMonthlyIncome')
plt.xticks([1], ['Logarithmic'], fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.suptitle('Before and After Logarithmic Comparison\n(MonthlyIncome)',
             fontproperties='Times New Roman', size=16)
plt.savefig('007_MonthlyIncome_box_Logarithmic_Comparison.png', dpi=1200)
plt.close()

data['LogDebtRatio'].hist(bins=100)
plt.title('Logarithmic DebtRatio', fontproperties='Times New Roman', size=16)
plt.xticks(fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('008_Logarithmic_DebtRatio_hist.png', dpi=1200)
plt.close()

data['LogRevolvingUtilizationOfUnsecuredLines'].hist(bins=100)
plt.title('Logarithmic RevolvingUtilizationOfUnsecuredLines',
          fontproperties='Times New Roman', size=14)
plt.xticks(fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('009_Logarithmic_RUOUL_hist.png', dpi=1200)
plt.close()

data['LogMonthlyIncome'].hist(bins=100)
plt.title('Logarithmic MonthlyIncome',
          fontproperties='Times New Roman', size=16)
plt.xticks(fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('010_Logarithmic_MonthlyIncome_hist.png', dpi=1200)
plt.close()

# 以上是数据预处理以及直观可视化

data['LowIncome'] = data['MonthlyIncome'] < 180
data['NormalIncome'] = data['MonthlyIncome'] >= 180
data[['LowIncome', 'NormalIncome']].sum().plot(kind='bar')
plt.xticks(rotation=0, fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.title('MonthlyIncome',
          fontproperties='Times New Roman', size=16)
plt.savefig('011_Income_binning.png', dpi=1200)
plt.close()

data['YoungAge'] = data['age'] < 24
data['OldAge'] = data['age'] > 65
data['NormalAge'] = (data['age'] <= 65) & (data['age'] >= 24)
data[['YoungAge', 'NormalAge', 'OldAge']].sum().plot(kind='bar')
plt.xticks(rotation=0, fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.title('Age',
          fontproperties='Times New Roman', size=16)
plt.savefig('012_Age_binning.png', dpi=1200)
plt.close()

# LogAge图像比较分立就弃了
# data=data[data['age']!=0]
#data['LogAge'] = np.log(data['age'])
# data.hist(column='LogAge',bins=100)
# plt.show()

data['LogIncomePerPerson'] = data['LogMonthlyIncome'] / \
    data['NumberOfDependents']
data.loc[~np.isfinite(data['LogIncomePerPerson']),
         'LogIncomePerPerson'] = np.nan
data['LogIncomePerPerson'].hist(bins=100)
plt.title('LogIncomePerPerson',
          fontproperties='Times New Roman', size=16)
plt.xticks(fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('013_LogIncomePerPerson.png', dpi=1200)
plt.close()

data['LogDebt'] = np.log(data['DebtRatio'] * data['LogMonthlyIncome'])
data.loc[~np.isfinite(data['LogDebt']), 'LogDebt'] = np.nan
data['LogDebt'].hist(bins=100)
plt.title('LogDebt',
          fontproperties='Times New Roman', size=16)
plt.xticks(fontproperties='Times New Roman', size=14)
plt.yticks(fontproperties='Times New Roman', size=14)
plt.savefig('014_LogDebt.png', dpi=1200)
plt.close()

# 以上为新增特征

original_data = pd.read_csv('cs-training.csv', index_col=0)
original_data = original_data[original_data['age'] != 0]
original_data = original_data[original_data['NumberOfTime30-59DaysPastDueNotWorse'] < 80]
plt.subplots(figsize=(15, 15))
seaborn.heatmap(original_data.corr(), annot=True,
                vmax=1, square=True, cmap='Blues')
plt.title('Heatmap', size=20)
plt.savefig('015_Heatmap.png', dpi=1200,bbox_inches=trs.Bbox([[-2,-1],[13,14]]))
plt.close()

# 以上为变量间相关关系
print('done')
