# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 6 - Bacteria growth table
# Date: 01/10/2026
# Description: Calculate exponential bacteria growth and display the output in a basic table format
base_bacteria = 200
hours = [0, 5, 10, 15]

print("Hour\tNumber of Bacteria")
for h in hours:
    # Bacteria doubles every hour: B = 200 * (2 ** h)
    B = base_bacteria * (2 ** h)
    print(f"{h}\t{B}")

print("\n EXTENDED EXERCISES ")
import matplotlib.pyplot as plt

# 1 & 2. Allow user input for maximum hour and step size
max_hour = int(input("Enter maximum hour (e.g., 20): "))
step_size = int(input("Enter step size (e.g., 5): "))

print("\nHour\tNumber of Bacteria (Dynamic)")
dynamic_hours = list(range(0, max_hour + 1, step_size))
bacteria_counts = []

for h in dynamic_hours:
    B = base_bacteria * (2 ** h)
    bacteria_counts.append(B)
    print(f"{h}\t{B}")

# 3. Plot the bacteria growth curve
print("\nGenerating bacteria growth curve...")
plt.figure(figsize=(8, 5))
plt.plot(dynamic_hours, bacteria_counts, marker='o', linestyle='-', color='red')
plt.title('Bacteria Growth Over Time')
plt.xlabel('Hour')
plt.ylabel('Number of Bacteria')
plt.grid(True)
plt.show()