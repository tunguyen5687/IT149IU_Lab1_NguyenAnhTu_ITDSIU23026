# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 2 - Fixing the input type
# Date: 01/10/2026
# Description: Fix a TypeError by properly casting string input to integer or float before calculation
number = int(input("Input a number between 1 and 10: "))
square = number * number
print("The square is:", square)

print("\n EXTENDED EXERCISES ")

# Allow multiple numbers (loop from 1 to 5) and check the range [1, 10]
for i in range(1, 6):
    num = int(input(f"[{i}/5] Input a number between 1 and 10: "))
    
    if 1 <= num <= 10:
        print("The square is:", num ** 2)
    else:
        print("Error: Number is out of range!")
