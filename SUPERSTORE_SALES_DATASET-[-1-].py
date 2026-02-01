#1ST KAGGLE DATASET.-[--SUPERSTORE_SALES_DATASET--] :-

import pandas as pd 
df=pd.read_csv("train.csv")
# print(df.columns)
# print(df.head().T)
print(df.iloc[:,0:3])