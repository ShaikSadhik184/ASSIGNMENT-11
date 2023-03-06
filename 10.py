def decimal_to_octal(decimal):
    """
    Convert decimal to octal representation
    """
    if decimal == 0:
        return 0
    octal_digits = []
    while decimal > 0:
        remainder = decimal % 8
        octal_digits.insert(0, str(remainder))
        decimal = decimal // 8
    return int(''.join(octal_digits))

# Example usage:
decimal_number = 123
octal_number = decimal_to_octal(decimal_number)
print(f"The octal representation of {decimal_number} is {octal_number}")
