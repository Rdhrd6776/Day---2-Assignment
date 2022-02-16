import numpy as np
import pandas as pd

from sklearn.datasets import load_diabetes
d= load_diabetes()
print(d)
df1=pd.DataFrames(d.data, colume.feature_name)
print(df1)
print(df1.head())
print(df1.tail())
print(df1.info())
print(df1.isnull().sum())