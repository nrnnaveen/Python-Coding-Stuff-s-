# Program to display n natural numbers and their sum

# Ask the user to input a value for n
n = int(input("Enter a number (n): "))

# Initialize sum
total_sum = 0

print(f"The first {n} natural numbers are:")

# Loop to print natural numbers and calculate the sum
for i in range(1, n + 1):
    print(i, end=' ')
    total_sum += i

# Print the sum
print(f"\nSum of first {n} natural numbers is: {total_sum}")
