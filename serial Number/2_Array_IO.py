import re

user = input("Enter numbers separated by spaces: ")

arr = []
for x in re.split(r'[,\s]+', user.strip()):
    arr.append(int(x))

for i in range(0, len(arr)):
    print(arr[i])