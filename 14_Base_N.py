print("Enter Decimal Number")
n = int(input())
# It will print binary, octal and hexadecimal of the given decimal number. and print like 0b1010, 0o12, 0xa respectively.

print("Binary Number is: ", bin(n))
print("Octal Number is: ", oct(n))
print("Hexadecimal Number is: ", hex(n))

# Now print like 1010, 12, a respectively.
print("Binary Number is: ", bin(n)[2:])
print("Octal Number is: ", oct(n)[2:])
print("Hexadecimal Number is: ", hex(n)[2:])