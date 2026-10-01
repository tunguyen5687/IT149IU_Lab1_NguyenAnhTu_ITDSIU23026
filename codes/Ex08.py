# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 8 - Name score with ord()
# Date: 01/10/2026
# Description: Calculate a name's score by summing the ASCII integer values of its characters
def name_score(name):
    return sum(ord(c) for c in name)

tom_score = name_score("Tom")
jim_score = name_score("Jim")

print("Tom score:", tom_score)
print("Jim score:", jim_score)

if tom_score > jim_score:
    print("Tom goes first!")
elif jim_score > tom_score:
    print("Jim goes first!")
else:
    print("It's a tie!")


print("\n EXTENDED EXERCISES ")

# 1. Write a function winner(names_list) to find the highest score
def winner(names_list):
    return max(names_list, key=name_score)

# 2. Allow user input of multiple names
user_input = input("Enter multiple names separated by space (e.g., Tom Jim Ada): ")

names_list = user_input.split()

# 3. Compute and display scores for all entered names
print("\nCalculating scores for entered names...")
for n in names_list:
    print(f"{n} score: {name_score(n)}")

if names_list:
    best_player = winner(names_list)
    print(f"\n=> {best_player} goes first with the highest score!")