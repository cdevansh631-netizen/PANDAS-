import pandas as pd
import numpy as np

#View first & last 3 rows
#Check shape, columns, data types
#Check missing values
#Fill missing Discount with 0
#Check & remove duplicates (if any)
#Create a new column Discount_Flag (Yes / No)
#Create Revenue column
#Create Cost column
#Create Profit column
#Create Profit_Margin (%)
#Total Revenue & Total Profit
#Product-wise total profit
#Region-wise average profit
#Top profit product
#Least profitable region
#Orders where Profit < 20,000
#Orders with Profit_Margin > 30%
#Sort orders by Profit (descendingOrders where Profit < 20,000
#Orders with Profit_Margin > 30%
#Sort orders by Profit (descending)
#Extract Year & Month
#Month-wise total sales
#Best month by profit
#Customer-wise total profit
#Which product sells best in North region?
#Does discount reduce profit? (logic answer)
df = pd.DataFrame({ 
    "Order_ID": [101,102,103,104,105,106,107,108,109,110],
    "Order_Date": [
        "2023-01-05","2023-01-15","2023-02-10","2023-02-20",
        "2023-03-05","2023-03-18","2023-04-02","2023-04-25",
        "2023-05-10","2023-05-28"
    ],
    "Customer": ["Amit","Neha","Ravi","Amit","Pooja","Neha","Ravi","Amit","Pooja","Neha"],
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop"],
    "Category": ["Electronics"] * 10,
    "Region": ["North","South","East","West","North","South","East","West","North","South"],
    "Units_Sold": [2,3,1,4,5,2,3,4,2,1],
    "Selling_Price": [60000,20000,30000,62000,21000,29000,61000,20500,29500,60000],
    "Cost_Price": [45000,15000,22000,47000,16000,23000,46000,15500,22500,45000],
    "Discount": [0,5,np.nan,10,0,5,np.nan,10,0,5]
})


#OVERVIEW:-
print(df.head(3),"\n")
print(df.tail(3),"\n")

#CHECKING OF SHAPE,COLUMN AND DATATYPE:-
print(df.info(),"\n")
print("(ROW,COLUMN):",df.shape."\n")

#MISSING VALUES:-
print(df.isnull().sum(),"\n")

#REMOVE DUPLICACY (IF ANY):-
df.drop_duplicates("Order_ID",inplace=True)

#REPLACE NAN VALUE IN DISCOUNT WITH 0:-
df.replace(np.nan,"0",inplace=True)