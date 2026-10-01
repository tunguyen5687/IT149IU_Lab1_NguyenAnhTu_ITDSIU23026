# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 7 - Right-aligned bacteria growth table
# Date: 01/10/2026
# Description: Format a table with precise right-aligned columns using f-string specifiers
base_bacteria = 200
hours = [0, 5, 10, 15]

print(f"{'Hour':>5} {'Number of Bacteria':>20}")
for h in hours:
    b = base_bacteria * (2 ** h)
    print(f"{h:>5} {b:>20}")


print("\n EXTENDED EXERCISES ")
import pandas as pd

# 1 & 2. Try different widths and add hours dynamically
print("1. Dynamic hours with different formatting widths (e.g., :>8 and :>15):")
dynamic_hours = [0, 5, 10, 15, 20, 24]
    
print(f"{'Hour':>8} {'Bacteria Count':>15}")
print("-" * 24)
    
# Initialize an empty list to store data for CSV export
data_records = []

for h in dynamic_hours:
    b = base_bacteria * (2 ** h)
    data_records.append({"Hour": h, "Number of Bacteria": b})
    print(f"{h:>8} {b:>15}")

# 3. Export the table to CSV using pandas
print("\n2. Exporting data to CSV...")
df = pd.DataFrame(data_records)
file_name = "bacteria_growth.csv"
df.to_csv(file_name, index=False)
    
print(f"Success! Data has been exported to '{file_name}'.")
print("\nHere is a preview of the exported DataFrame:")
print(df)
