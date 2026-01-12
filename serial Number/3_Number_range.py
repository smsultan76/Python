# Input Number like 10-20
num = input("Enter a number range (e.g., 10-20): ")

arr = []

n1 = int(num.split("-")[0].strip())
n2 = int(num.split("-")[1].strip())

for i in range(n1, n2):
    arr.append(i)

print(arr)