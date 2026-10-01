# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 13 - BMI calculator
# Date: 01/10/2026
# Description: Calculate BMI from weight and height, then determine the health category
print(" EXERCISE 13: BMI CALCULATOR ")

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI = {bmi:.1f} -> {category}")
