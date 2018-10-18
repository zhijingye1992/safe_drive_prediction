import pandas as pd
df = pd.read_csv('/Users/ZhijingYe/Documents/ipython_notebook/HW/practice/Safe_Driver_Prediction/data/train.csv',
                 index_col=False)
print(df.head())

from sklearn import linear_model