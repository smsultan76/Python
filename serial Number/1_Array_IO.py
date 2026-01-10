user = input("Enter numbers separated by spaces: ")

arr = []
for x in user.split(","):
    arr.append(int(x))

for i in range(0, len(arr)):
    print(arr[i])