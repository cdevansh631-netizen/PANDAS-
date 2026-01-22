#PANDAS NOTES :


#1-Creating a DataFrame:
import pandas as pd
# Data={"Name":["Dev","Raj","Anaya","Manay"],"Roll_No":[43,54,23,91],"Subject":["Chem","Physics","Math","Yoga"]}
# print(pd.DataFrame(Data))


#2-Reading a File-:
#-it only read plain file ie csv,excel-:
# print(pd.read_csv("Book1.csv"))

#3-Exploring Data in csv:-
data=pd.read_csv("Book1.csv")
# print(data.head(1))            #1st row only
# print(data.tail(2))            #Last 2
# print(data.info())               #Dtype ie info
# print(data.describe())
print(data.isnull().sum())        #It tell wheather any column have null value or not