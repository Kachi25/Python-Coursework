# Create a random list of numbers
numbers = [34, 76, 45, 90, 11]
print("Original list:", numbers)

# Bubble sort algorithm to sort the list in ascending order
n = len(numbers)

# Outter loop for each pass through the list
for i in range(n):
    # Inner loop for comparing adjacent elements
    for j in range(0, n-i-1):
        # Compare the adjacent elements
        if numbers[j] > numbers[j+1]:
            # Swap if the element found is greater than the next element
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# Display the sorted list
print("List after bubble sort:", numbers)

