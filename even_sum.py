# Start the sum variable at 0.for loop
total_sum = 0

#using the for loop
for i in range(1, 51):  # Loop through numbers from 1 to 50 
    # Check if the number is even
    if i % 2 == 0:
        total_sum += i  # Add the even number to the total sum

print(f"The sum of even numbers from 1 to 50 is: {total_sum}")

# with while loop
number = 1
total_sum_while = 0

while number <= 50:
    if number % 2 == 0:
        total_sum_while += number
    number += 1

print(f"The sum of even numbers from 1 to 50 (using while loop) is: {total_sum_while}")
