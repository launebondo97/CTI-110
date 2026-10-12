# Laurent Munsi Bondo
# October 09,2026
# P3HW2_Laurent Munsi Bondo
# This program calculates regular pay, overtime pay, and gross pay

# Get user inputs
name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate pay
if hours_worked <= 40:
    reg_pay = hours_worked * pay_rate
    overtime_pay = 0.0
else:
    reg_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

gross_pay = reg_pay + overtime_pay

# Display results
print("-" * 30)
print(f"Employee name: {name}")
print(f"Hours Worked: {hours_worked}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Overtime Hours: {max(0, hours_worked - 40)}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${reg_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
