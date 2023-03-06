n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n*2, 2):
    sum += i
print("The sum of first", n, "odd natural numbers is", sum)
