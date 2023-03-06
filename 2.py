n = int(input("Enter the value of N: ")) # Taking input from user for N
sum = 0

# Loop to calculate sum of squares of first N natural numbers
for i in range(1, n+1):
    sum += i**2

print("Sum of squares of first", n, "natural numbers is", sum)
