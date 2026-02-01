#1ST KAGGLE DATASET.-[--SUPERSTORE_SALES_DATASET--] :-
import pandas as pd
 
df=pd.read_csv("train.csv")
print(df.columns)


import pandas as pd 
df=pd.read_csv("train.csv")
print(df.columns)

#UNDERSTANDING DATA:-
print("NDERSTANDING DATA:-","\n")
print("COLUMNS :-",df.columns,"\n")
print("DATA TYPE :-",df.info(),"\n")
print(df.describe(include="object"))
print("(ROWS,COLUMN) :-",df.shape,"\n")


# #DATA HANDLING :-
# print(df.isnull().sum())
# # print(df.drop_duplicates())
# print(df.isnull.sum())
