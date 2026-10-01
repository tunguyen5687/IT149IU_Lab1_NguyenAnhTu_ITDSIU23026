# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 14 - Cash withdrawal (//, %)
# Date: 01/10/2026
# Description: Determine the minimum number of ATM notes needed for a specific withdrawal amount
amount = int(input("Amount (VND): "))
notes_500k = amount // 500000
amount = amount % 500000
notes_200k = amount // 200000
amount = amount % 200000
notes_100k = amount // 100000
amount = amount % 100000
notes_50k = amount // 50000

print(f"500,000 x {notes_500k}")
print(f"200,000 x {notes_200k}")
print(f"100,000 x {notes_100k}")
print(f" 50,000 x {notes_50k}")