n = int(input("Enter the value of N: "))  # take input from the user

sum = 0  # initialize sum to 0

for i in range(1, n + 1):
    sum += i

print(f"The sum of first {n} natural numbers is {sum}")
