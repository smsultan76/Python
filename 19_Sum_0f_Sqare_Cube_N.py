# Sum of Square and Cube of first n natural numbers
# 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + ... + n^2
# 1^3 + 2^3 + 3^3 + 4^3 + 5^3 + ... + n^3
# Using loop. complexity n!

class Sum:
    def __init__(self,n):
        self.n = n
        self.sum = 0
    def square(self):
        if self.n < 0:
            return "Failed"
        else:
            sum_square = 0
            for i in range(1, self.n + 1):
                sum_square += i**2
            return sum_square

    def cube(self):
        if self.n < 0:
            return "Failed"
        else:
            sum_cube = 0
            for i in range(1, self.n + 1):
                sum_cube += i**3
            return sum_cube

    def __str__(self):
        return f"Result for Sum of Square:    {self.square()}   and Sum of Cube:      {self.cube()}"

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(Sum(n))
            