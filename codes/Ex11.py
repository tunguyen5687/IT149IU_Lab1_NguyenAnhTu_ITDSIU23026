# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 11 - Employee wage growth / decline
# Date: 01/10/2026
# Description: Calculate compound wage growth and decline over multiple years using exponentiation
o = 10.0

p_good, n_good = 0.03, 5 
w_good = o * (1 + p_good) ** n_good
print('After 5 years good reviews:', round(w_good, 2))

p_bad = -0.03
n_bad = 2
w_bad = o * (1 + p_bad) ** n_bad
print('After 2 years bad reviews:', round(w_bad, 2))


print("\n EXTENDED EXERCISES ")
import matplotlib.pyplot as plt

# 1. Let the user input o, p, and n; compute the final wage.
print("1. Dynamic Wage Calculator:")
user_o = float(input("Enter original hourly wage ($): "))
user_p = float(input("Enter percentage change (e.g., 0.03 for 3% raise, -0.03 for 3% cut): "))
user_n = int(input("Enter number of years: "))

user_w = user_o * (1 + user_p) ** user_n
print(f"-> Final wage after {user_n} years: {round(user_w, 2)}")

# 2. Accept a sequence of reviews and apply 1.03 or 0.97 each year.
print("\n2. Sequence of Reviews:")
reviews = ['good', 'bad', 'good', 'good', 'bad']
current_wage = user_o
wage_history = [current_wage]  

print(f"Starting wage: {current_wage:.2f}")
for year, review in enumerate(reviews, start=1):
    if review == 'good':
        current_wage *= 1.03  
    elif review == 'bad':
        current_wage *= 0.97  
    
    wage_history.append(current_wage)
    print(f"Year {year} ({review}): {current_wage:.2f}")

# 3. Plot wage-by-year using matplotlib to visualize the compounding effect.
print("\n3. Generating wage trend chart...")

years = list(range(len(wage_history)))

plt.figure(figsize=(8, 5))
plt.plot(years, wage_history, marker='o', linestyle='-', color='green')

plt.title('Employee Wage Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Hourly Wage ($)')
plt.xticks(years)
plt.grid(True)
plt.show()