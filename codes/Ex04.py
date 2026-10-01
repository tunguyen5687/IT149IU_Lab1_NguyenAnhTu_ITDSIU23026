# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 4 - Eggs in boxes
# Date: 01/10/2026
# Description: Calculate box capacity and remainder using floor division and modulo operations
eggs = 28
per_box = 6

boxes = eggs // per_box + (1 if eggs % per_box else 0)
last_box_fill = eggs % per_box if eggs % per_box else per_box
need_to_fill_last = per_box - (eggs % per_box) if eggs % per_box else 0

print("Total eggs:", eggs)
print("Boxes needed:", boxes)
print("Eggs in last box:", last_box_fill)
print("Eggs needed to fill last box:", need_to_fill_last)

print("\n EXTENDED EXERCISES ")

# 1. Allow user input for eggs and per_box
eggs_ext = int(input("Input total number of eggs: "))
per_box_ext = int(input("Input capacity of each box: "))

boxes_ext = eggs_ext // per_box_ext + (1 if eggs_ext % per_box_ext else 0)
last_fill_ext = eggs_ext % per_box_ext if eggs_ext % per_box_ext else per_box_ext
need_fill_ext = per_box_ext - (eggs_ext % per_box_ext) if eggs_ext % per_box_ext else 0

print("Total eggs:", eggs_ext)
print("Boxes needed:", boxes_ext)
print("Eggs in last box:", last_fill_ext)
print("Eggs needed to fill last box:", need_fill_ext)

# 2. Draw an ASCII diagram showing boxes and eggs
print("\nASCII Diagram:")
print("('O' = has egg, '.' = empty space)")

full_boxes = eggs_ext // per_box_ext
remainder = eggs_ext % per_box_ext

# Print full boxes
for _ in range(full_boxes):
    print("[" + " O" * per_box_ext + " ]")

# Print the remaining box
if remainder > 0:
    print("[" + " O" * remainder + " ." * need_fill_ext + " ]")