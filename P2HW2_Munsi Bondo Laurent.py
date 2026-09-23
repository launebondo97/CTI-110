# Laurent Munsi Bondo
# September 23, 2026
# P2HW2_Assignment
# Write a program that asks the user to enter test grades for 6 modules, using a separate input statement for each one.

# Step 2: Prompt for grades using separate input statements
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Step 3: Store all six grades in a descriptive list
module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Step 4: Calculate required results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Step 5: Display formatted results
print("\n------------Results------------")
print(f"Lowest Grade:       {lowest_grade:.1f}")
print(f"Highest Grade:      {highest_grade:.1f}")
print(f"Sum of Grades:      {sum_of_grades:.1f}")
print(f"Average:            {average_grade:.2f}")
print("---------------------------------")

