# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 15 - Digits of a number
# Date: 01/10/2026
# Description: Extract digits, calculate their sum, and reverse a three-digit integer mathematically
num = int(input("Enter a three-digit integer (e.g., 472): "))

hundreds = num // 100
tens = (num % 100) // 10
units = num % 10

sum_digits = hundreds + tens + units
reversed_num = (units * 100) + (tens * 10) + hundreds

print(f"Hundreds: {hundreds}, Tens: {tens}, Units: {units}")
print(f"Sum of digits: {sum_digits}")
print(f"Reversed number: {reversed_num}")

if num == reversed_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")