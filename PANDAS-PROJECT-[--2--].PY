# MINI PROJECT 2:--[--EMPLOYEE PERFORMANCEE ANALYZER--]

# 🟡 Basic Understanding
#-1-View the dataset
#-2-Check data types
#-3-Get basic statistics

# 🟡 Core Analysis
#-4-Add Bonus column
#-5-If Performance_Score >= 85 → Bonus = 10% of Salary
#-6-Else → Bonus = 5% of Salary
#-7-Add Total_Compensation
#-8-Salary + Bonus

# 🟡 Performance Analysis
#-9-Find Top Performer
#-10-Find Lowest Performer
#-11-List employees with Performance < 60
#-12-Count how many employees are underperforming

# 🟡 Group Analysis
#-13-Department-wise average salary
#-14-Department-wise top performer

# 🟡 Sorting & Filtering
#-15-Sort employees by Total_Compensation (desc)
#-16-List employees earning more than 50,000 salary

#🟡 Thinking Like Analyst 🧠 (IMPORTANT)
# -17-Which department is most expensive (highest avg salary)?
# -18-Which employee gives best value for money.


import pandas as pd

df = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Neha", "Rohit", "Priya", "Karan", "Anjali"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Experience": [2, 5, 3, 7, 1, 4],   
    "Performance_Score": [78, 88, 65, 92, 55, 81],
    "Salary": [40000, 55000, 42000, 75000, 38000, 60000]
})

#BASIC IDEA :--
# print(df)
# print(df.info())

#ADDING BONUS NEW COLUMN:--
df.loc[df["Performance_Score"]>=85,"Bonus"]=0.1*df["Salary"]
df.loc[df["Performance_Score"]<85,"Bonus"]=0.05*df["Salary"]
# print(df)

#Total compensations:
df['Total Compensation']=df["Salary"]+df["Bonus"]
print(df,"\n")

#Top/Least Performer:--
print("TOP PERFORMER :--")
print(df.loc[df["Performance_Score"]==df["Performance_Score"].max(),"Name"].to_string(index=False))
 
print("LEAST PERFORMER :--")
print(df.loc[df["Performance_Score"]==df["Performance_Score"].min(),"Name"].to_string(index=False),"\n")


#List oof Employee HAving Performance <60:
print("STUDENT HAVING PERFORMANCE LESS THAN 60:--")
print(df.loc[df["Performance_Score"]<60,"Name"].to_string(index=False))
print("NO OF STUDENT UNDERPERFORMING :",df.loc[df["Performance_Score"]<60,"Name"].count(),"\n")


#Department Wise Average Salary:
print(df.groupby("Department").agg({"Salary":"mean"}))

#Department Wise Top Performer:-
print()
