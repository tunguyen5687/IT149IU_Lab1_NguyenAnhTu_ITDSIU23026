# Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: IT149IU - Fundamentals of Programming
# Lab: Lab 1
# Task: Exercise 10 - Seconds to hours - minutes - seconds
# Date: 01/10/2026
# Description: Convert total seconds into hours, minutes, and seconds using modulo and floor division
total_seconds = int(input("Enter a number of seconds (> 3600): "))
hours = total_seconds // 3600
remainder = total_seconds % 3600
minutes = remainder // 60
seconds = remainder % 60
print("Output:", hours, minutes, seconds, sep=" - ")


print("\n EXTENDED EXERCISES ")

# 1. Validate that the input is > 3600
if total_seconds <= 3600:
    print("Warning: The input should be greater than 3600 seconds.")
else:
    print("Validation: Input is valid (> 3600).")

# 2. Print the time as HH:MM:SS with zero padding (02d)
print(f"Time format: {hours:02d}:{minutes:02d}:{seconds:02d}")

# 3. Convert back and check if it matches the original input
converted_back = hours * 3600 + minutes * 60 + seconds
is_match = (converted_back == total_seconds)

print(f"Check math: {hours}*3600 + {minutes}*60 + {seconds} = {converted_back}")
print(f"Is match correct? {is_match}")