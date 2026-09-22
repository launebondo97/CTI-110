# Laurent Munsi Bondo
# 09.22.2026
# P2LAB2.py
# Using dictionaries
 
Cars={'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}
# Get keys from dictionary
Cars_keys =Cars.keys()
print(Cars_keys)
print(* Cars_keys, sep=",")
# Get a car from user
car_name= input("Enter a car: ")
# Get mpg for the given car
car_mpg= Cars[car_name]
print(f"The {car_name} get {car_mpg} miles per gallon.")
# Get miles from user
miles_driven= float(input(f"How many miles will you drive the {car_name}?"))
# Calculate
gallons_needed= miles_driven/ car_mpg
# Dispaly results
print(f"{gallons_needed: .2f} gallon(s) of gaz are needed to drive the {car_name} {miles_driven} miles")

