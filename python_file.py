
# Simple Python program: Sum of even numbers in a list

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize sum
even_sum = 0

# Loop through the list
for num in numbers:
    if num % 2 == 0:  # Check if number is even
        even_sum += num

# Print the result
print("Sum of even numbers:", even_sum)

