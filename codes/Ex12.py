# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 12 - Sorting runner times with if only
# Date: 01/10/2026
# Description: Sort three floating-point numbers in ascending order by using exhaustive if statements
a = float(input('Enter time for runner 1: '))
b = float(input('Enter time for runner 2: '))
c = float(input('Enter time for runner 3: '))

print('Times in ascending order:')
if a <= b and b <= c: print(a, b, c)
if a <= c and c <= b: print(a, c, b)
if b <= a and a <= c: print(b, a, c)
if b <= c and c <= a: print(b, c, a)
if c <= a and a <= b: print(c, a, b)
if c <= b and b <= a: print(c, b, a)


print("\n EXTENDED EXERCISES ")
print("1. Fix duplicate-printing bug and announce the winner")

a_ext = float(input('Enter time for runner 1: '))
b_ext = float(input('Enter time for runner 2: '))
c_ext = float(input('Enter time for runner 3: '))

print('Times in ascending order (Strict comparisons):')

# Using strict comparisons (<) for overlapping cases to prevent duplicate prints
if a_ext <= b_ext and b_ext <= c_ext:
    print(a_ext, b_ext, c_ext)
    print("-> Winner: Runner 1")
    
if a_ext <= c_ext and c_ext < b_ext:
    print(a_ext, c_ext, b_ext)
    print("-> Winner: Runner 1")
    
if b_ext < a_ext and a_ext <= c_ext:
    print(b_ext, a_ext, c_ext)
    print("-> Winner: Runner 2")
    
if b_ext <= c_ext and c_ext < a_ext:
    print(b_ext, c_ext, a_ext)
    print("-> Winner: Runner 2")
    
if c_ext < a_ext and a_ext <= b_ext:
    print(c_ext, a_ext, b_ext)
    print("-> Winner: Runner 3")
    
if c_ext < b_ext and b_ext < a_ext:
    print(c_ext, b_ext, a_ext)
    print("-> Winner: Runner 3")