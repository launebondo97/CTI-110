# Laurent Munsi Bondo
# October 09,2026
# P3HW1_Laurent Munsi Bondo
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Add grades entered to a list

module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]
# TO DO: determine lowest, highest , sum and average for grades

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Display formatted results

print("\n------------Results------------")
print(f"{'Lowest Grade:':<18}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<18}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<18}{sum_of_grades:.1f}")
print(f"{'Average:':<18}{average_grade:.1f}")
print("---------------------------------")

# determine letter grade for average

if average_grade>= 90:
        letter_grade = "A"
elif average_grade>= 80:
        letter_grade = "B"
elif average_grade>= 70:
        letter_grade = "C"
elif average_grade>= 60:
        letter_grade = "D"
else:
        letter_grade = "F"
print(f"Your grade is: {letter_grade}")