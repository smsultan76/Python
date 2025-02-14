def Sum_With_Formula(n):
    return n*(n+1)//2

def Sum_With_Loop(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def main():
    n = int(input("Enter a number: "))
    print("Sum using formula: ", Sum_With_Formula(n))
    print()
    print("Sum using loop: ", Sum_With_Loop(n))


if __name__ == "__main__":
    main()