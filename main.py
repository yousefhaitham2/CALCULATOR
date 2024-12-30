# main.py

# Taking the first input from the user and storing it in 'first_number'
first_number = float(input("Enter the first number: "))

# Taking the second input from the user and storing it in 'second_number'
second_number = float(input("Enter the second number: "))

# Performing arithmetic operations
sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number

# Checking for division by zero
if second_number != 0:
    division_result = first_number / second_number
else:
    division_result = "undefined (cannot divide by zero)"

# Printing the results
print("Sum:", sum_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)
