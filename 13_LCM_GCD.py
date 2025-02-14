def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm
def gcd(x,y):
    while y:
        x, y = y, x % y
    return x

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))
    print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))