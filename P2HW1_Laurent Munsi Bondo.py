# Laurent Munsi Bondo
# September 22, 2026
# P2HW1_Laurent Munsi Bondo
# my project consists of creating a budget calculator that formats travel expenses into a clean, aligned column layout.
# Step 3: Ask user to enter their budget
budget = float(input("Enter Budget: "))
# Step 4: Ask user to enter travel destination
destination = input("Enter your travel destination: ")
# Step 5: Ask user for amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas? "))
# Step 6: Ask user for amount they will spend on accommodation
hotel_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
# Step 7: Ask user for amount they will spend on food
food_expense = float(input("Last, how much do you need for food? "))
# Step 8: Add expenses
total_expenses = gas_expense + hotel_expense + food_expense
# Step 9: Subtract expenses from budget
remaining_balance = budget - total_expenses
# Step 10: Display formatted results
print("\n------------Travel Expenses------------")
print(f"{'Location:':<25}{destination}")
print(f"{'Initial Budget:':<25}${budget:.2f}")
print(f"{'Fuel:':<25}${gas_expense:.2f}")
print(f"{'Accommodation:':<25}${hotel_expense:.2f}")
print(f"{'Food:':<25}${food_expense:.2f}")
print("---------------------------------------")
print(f"{'Total Expenses:':<25}${total_expenses:.2f}")
print(f"{'Remaining Balance:':<25}${remaining_balance:.2f}")

