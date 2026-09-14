# Laurent Munsi Bondo
# 09.13.2026
# p1hw2.py
# my project consists to create a program that does some basic math on numbers that are entered

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
# Step 10: Display results
print("\n------------Travel Expenses------------")
print(f"Location:          {destination}")
print(f"Initial Budget:    {budget:.2f}")
print(f"Fuel:              {gas_expense:.2f}")
print(f"Accommodation:     {hotel_expense:.2f}")
print(f"Food:              {food_expense:.2f}")
print("---------------------------------------")
print(f"Total Expenses:    {total_expenses:.2f}")
print(f"Remaining Balance: {remaining_balance:.2f}")

