# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 3 - Arithmetic operators
# Date: 01/10/2026
# Description: Test basic arithmetic operators including floor division and exponentiation
print("\n Exercise 3 ")

left_operands = [-5, 0, 5, 7.5]
right_operand = 2   

for a in left_operands:
    print(f"\n Testing with left operand = {a} ")
    print(a, "+", right_operand, "=", a + right_operand)
    print(a, "-", right_operand, "=", a - right_operand)
    print(a, "*", right_operand, "=", a * right_operand)
# Compare / vs // on negative numbers
    print(a, "/", right_operand, "=", a / right_operand)
    print(a, "//", right_operand, "=", a // right_operand)
    print(a, "**", right_operand, "=", a ** right_operand)

print("\n EXTENDED EXERCISES ")
# Compute square roots via exponent
b = 25
print(f"Square root of {b} via exponent: {b ** 0.5}")

# Format results with f-strings to align columns nicely. 
print("\nFormatted Table (f-strings):")
print(f"{'a':<6} {'op':<4} {'b':<4} {'=':<2} {'Result':>8}")

for a in left_operands:
    print(f"{a:<6} {'+':<4} {right_operand:<4} {'=':<2} {a + right_operand:>8}")
    print(f"{a:<6} {'-':<4} {right_operand:<4} {'=':<2} {a - right_operand:>8}")
    print(f"{a:<6} {'*':<4} {right_operand:<4} {'=':<2} {a * right_operand:>8}")
    print(f"{a:<6} {'/':<4} {right_operand:<4} {'=':<2} {a / right_operand:>8}")
    print(f"{a:<6} {'//':<4} {right_operand:<4} {'=':<2} {a // right_operand:>8}")
    print(f"{a:<6} {'**':<4} {right_operand:<4} {'=':<2} {a ** right_operand:>8}")