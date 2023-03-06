# function to calculate factorial
def factorial(n):
    # initialize the result variable
    result = 1

    # loop through all the numbers from n down to 1
    for i in range(n, 0, -1):
        # multiply the result by the current number
        result *= i

    # return the final result
    return result

# example usage
n = 6
fact = factorial(n)
print(f"The factorial of {n} is {fact}")
