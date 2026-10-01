# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 1 - Variables and print()
# Date: 01/10/2026
# Description: Demonstrate variable assignment and various print function formatting techniques
x = 2
y = 3

print('a) x =', x)
print('b) Value of', x, '+', x, 'is', (x + x))
print('c) x =')
print('d)', (x + y), '=', (y + x))

print("\n EXTENDED EXERCISES ")
x = 7
y = 9
print("1. Re-run with x=7, y=9:")
print('a) x =', x)
print('b) Value of', x, '+', x, 'is', (x + x))
print('c) x =')
print('d)', (x + y), '=', (y + x))

# 2. Using sep argument 
print("\n2. Using sep argument:")
print('x=', x, sep='')

# 3. Use the end argument
print("\n3. Using end argument:")
print('x=', x, end='; ')
print('y=', y)

# 4. Using f-strings
print("\n4. Rewrite using f-strings:")
print(f"x = {x}")