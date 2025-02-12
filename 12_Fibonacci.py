def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))

    # fibonacci in Normal way

    a = 0
    b = 1
    print("Fibonacci series:")
    for i in range(n):
        print(a, end = " ")
        c = a + b
        a = b
        b = c
    print()
    

    # fibonacci using recursion

    print("Fibonacci series using recursion:")
    for i in range(n):
        print(fibonacci(i), end = " ")
    print()
    print(fibonacci(n-3))


