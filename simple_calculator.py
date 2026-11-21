# Ask a user to input two numbers
number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")

#check if the numbers are valid
if number_1.replace(".", "", 1).isdigit() and number_2.replace(".", "", 1).isdigit():
    number_1 = float(number_1)
    number_2 = float(number_2)
else:
    print("Error: You did not enter 2 numbers")
    exit()      

# Ask the user to input an operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    if number_2 != 0:
        result = number_1 / number_2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

# Display the result
print(f"The result is: {number_1} {operation} {number_2}={result}")
