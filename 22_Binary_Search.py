def Binary_Search(arr, x):
    left =0
    right = len(arr)-1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements: ").strip().split()))
    arr.sort()
    print("Sorted array: ", arr)
    x = int(input("Enter the element to search: "))
    result = Binary_Search(arr, x)
    if result != -1:
        print("Element is present at index %d" % result)
    else:
        print("Element is not present in array")