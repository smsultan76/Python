class mul:
    def __init__(self, num):
        self.num = num
    def table(self):
        for i in range(1, 11):
            print(f"{self.num} * {i} = {self.num*i}")

if __name__ == "__main__":
    n = int(input("Enter the number for which you want to print the table: "))
    mul(n).table()