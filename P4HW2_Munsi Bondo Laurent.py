# Laurent Munsi Bondo
# October 20,2026
# P4HW2_Laurent Munsi Bondo
# This program will use a loop to calculates regular pay, overtime pay, and gross pay
# Request Employee info
name = input("Enter employee's name or 'done' to finish: ")

# Create Accumulator Variables for overtime pay,regular pay,gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    # Add employee count plus one
    employee_count += 1 # employee_count = employee_count + 1
    # Ask for employee info
    hours = float(input("How many hours did "+name+" work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))
    
    # Evaluate overtime
    if hours >40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    # Add to accumulator totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display results for this employee
    print("--------------------------")
    print("Employee name: ", name)
    print(f'{"hours worked":<15}{"pay rate":<12}{"0vertime pay":<15}{"regular pay":<15}{"gross pay":<12}')
    print("----------------------------------------------------------------------")     
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))
