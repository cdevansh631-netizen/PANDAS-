# MINI PROJECT 3:--[--PRODUCT SALES AND PROFIT ANALYZER--]:--

#1-> View the dataset
#2-> Check data types
#3-> Get basic statistics
#4-> Add Revenue column
#5-> Add Cost Column
#6-> Add profit column
#7-> Add Profit Margin.
#8-> Find Top Profit Product
#9-> Find Lowest Profit Product
#10-> List products with Profit < 50,000
#11-> Count how many low-profit entries
#12-> Category-wise total revenue
#13-> Product-wise average profit
#14-> Region-wise top profit product
#15-> Sort orders by Profit (descending)
#16-> List orders where Profit_Margin > 25%
#17-> Which product is most profitable overall?
#18-> Which region is least profitable?
#19-> Which product gives best value for money?




import pandas as pd

df = pd.DataFrame({
    "Order_ID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Units_Sold": [5, 10, 6, 4, 12, 7, 3, 9],
    "Selling_Price": [60000, 20000, 30000, 62000, 21000, 29000, 61000, 20500],
    "Cost_Price": [45000, 15000, 22000, 47000, 16000, 23000, 46000, 15500]
})
