n = int(input("Enter the value of N: "))
sum_of_cubes = 0

for i in range(1, n+1):
    sum_of_cubes += i ** 3

print("The sum of cubes of first", n, "natural numbers is:", sum_of_cubes)
