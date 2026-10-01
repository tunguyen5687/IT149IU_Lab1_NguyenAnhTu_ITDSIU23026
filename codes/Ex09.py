# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 9 - Course grades (average, best, worst)
# Date: 01/10/2026
# Description: Store grades in a dictionary and find the average, highest, and lowest courses
courses = {}
courses['Math'] = int(input('Enter grade for Math: '))
courses['Physics'] = int(input('Enter grade for Physics: '))
courses['AI'] = int(input('Enter grade for AI: '))

avg = sum(courses.values()) / len(courses)
best = max(courses, key=courses.get)
worst = min(courses, key=courses.get)

print('Average grade:', round(avg, 2))
print('Highest grade:', best, courses[best])
print('Lowest grade:', worst, courses[worst])


print("\n EXTENDED EXERCISES ")
import pandas as pd

# 1. Allow any number of courses until the user types 'done'
print("1. Dynamic course grade entry (type 'done' to finish):")
dynamic_courses = {}

while True:
    course_name = input("Enter course name (or 'done' to stop): ")
    if course_name.lower() == 'done':
        break
    
    grade_val = int(input(f"Enter grade for {course_name}: "))
    dynamic_courses[course_name] = grade_val

if dynamic_courses:
    # 2. Save the results to a CSV file for later analysis
    print("\n2. Saving results to CSV...")
    
    grades_series = pd.Series(dynamic_courses, name="Grade")
    df_grades = grades_series.reset_index()
    df_grades.columns = ["Course", "Grade"]
    
    csv_filename = "course_grades.csv"
    df_grades.to_csv(csv_filename, index=False)
    print(f"Data successfully saved to '{csv_filename}'.")
    
    # 3. Use pandas Series describe() to summarize statistics (mean, min, max, std, etc.)
    print("\n3. Statistical summary using pandas.Series.describe():")
    print(grades_series.describe())
else:
    print("No courses were entered.")
