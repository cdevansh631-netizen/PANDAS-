#PANDAS NOTES :
import pandas as pd


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
data=pd.read_excel("Duplicate.xlsx")
# print(data)
# print(data.isnull()) #To Find any null value or not.
# print(data.isnull().sum())  #give sum of no of nul value in column.
print(data.dropna())   #drop a row if any clumn caary null value.
