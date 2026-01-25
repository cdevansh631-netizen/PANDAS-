#PANDAS NOTES :
import pandas as pd
import numpy as np


#1-Creating a DataFrame:

# Data={"Name":["Dev","Raj","Anaya","Manay"],"Roll_No":[43,54,23,91],"Subject":["Chem","Physics","Math","Yoga"]}
# print(pd.DataFrame(Data))




#2-Reading a File-:
# -it only read plain file ie csv,excel-:
# print(pd.read_csv("Book1.csv"))




#3-Exploring Data in csv:-
# data=pd.read_csv("Book1.csv")
# print(data.head(1))            #1st row only
# print(data.tail(2))            #Last 2
# print(data.info())               #Dtype ie info
# print(data.describe())
# print(data.isnull().sum())        #It tell wheather any cotent have null value or not




#4-Handling Duplicate Value in python:-

# data=pd.read_excel("Duplicate.xlsx")
#Drop on bases of Primary Key Only:--
# print(data.drop_duplicates("Emplyee id"))




#5..Working With Missing data in python:
# data=pd.read_excel("Duplicate.xlsx")
# print(data)
# print(data.isnull().sum())  #give sum of no of nul value in column.
# print(data.dropna())   #drop a row if any clumn caary null value.
# print(data.replace(np.nan,"69%"))    #It Replace all nan value 69%

#What if i want to replace nan only at one column at which nan occur.
# data["Math"]=data["Math"].replace(np.nan,"68%")
# print(data)
# print(data.fillna(method="bfill")) #It fill nan value with nxt value to it.
# print(data.fillna(method="ffill"))  #It fill nan value with value come before to it.





#6--Column Transformation :--
#1--
#It create a new column and give BONUS/No BONUS based on that that it get or not.
# df=pd.read_excel("Duplicate.xlsx")
# df.loc[(df["Bonus"]==0),"Get Bonus"]="No Bonus"
# df.loc[(df["Bonus"]>0),"Get Bonus"]="Bonus"
# print(df)

#2--
# data=pd.read_excel("Duplicate.xlsx")
# data["Full name"]=data["name"].str.capitalize()+" "+data["last name"]    #IT ceate a new column of full name.
# print(data)

#3--
# data=pd.DataFrame({"Month":["January","Febraury","MArch","April"]})
# def extract(value):
#     return value[0:3]
# data["Short month"]=data["Month"].map(extract)
# print(data)





#7:----Group by in Pandas:--
df=pd.DataFrame({"Chemistry":["Organic","Inorganic","Inorganic","Organic","Inorganic"],
                 "Gender":["Male","Female","Female","Male","Female"]})
# gp=df.groupby("Chemistry").agg({"Gender":"count"})
# gp=df.groupby(["Chemistry","Gender"]).size()
# print(gp)
