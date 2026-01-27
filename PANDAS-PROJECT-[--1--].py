# 🔹 Basic Understanding
# View the dataset
# Check column names & data types
# Get basic statistics
# 🔹 Core Analysis
# Add Total Marks column
# Add Average Marks column
# Find the Topper
# Find the Lowest scorer
# 🔹 Performance Analysis
# List students who failed (avg < 60)
# Count how many students failed
# Find subject-wise average marks
# 🔹 Group Analysis
# Gender-wise average marks
# Gender-wise topper
# 🔹 Sorting & Filtering
# Sort students by total marks (highest first)
# List students scoring more than 85 in any subject
# 🔹 Thinking Like Analyst (Important)
# Which subject is most difficult? (lowest average)
# Which student is most consistent? (smallest marks difference)


#MINI PROJECT 1: STUDENT PERFORMANCE ANALYZER:-[--🎯 Your Goal Understand the data and answer simple questions using Pandas--]
import pandas as pd

data = pd.DataFrame({
    "Name": ["Dev", "Aman", "Riya", "Neha", "Rahul"],
    "Math": [78, 85, 67, 90, 56],
    "Science": [72, 88, 70, 95, 60],
    "English": [80, 75, 68, 92, 58],
    "Gender": ["Male", "Male", "Female", "Female", "Male"]
})
