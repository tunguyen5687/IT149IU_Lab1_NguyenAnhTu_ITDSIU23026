# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 5 - Odd or even with the remainder operator
# Date: 01/10/2026
# Description: Determine if an integer is odd or even using an if statement and modulo operator
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

print("\n EXTENDED EXERCISES ")

print("1. Classification for numbers 1-10:")
# Use range(1, 11) because the stop value (11) is always excluded
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print("\n2. Pandas DataFrame filtering by index:")
import pandas as pd

# Create a sample DataFrame with 5 people
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nFiltered DataFrame (Keep only rows with an even index):")
# Filter by checking if the index modulo 2 equals 0
even_df = df[df.index % 2 == 0]
print(even_df)
