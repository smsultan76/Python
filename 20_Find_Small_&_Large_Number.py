class large:
    def __init__(self,arr):
        self.arr = arr
    def find_large(self):
        large = self.arr[0]
        for i in range(1,len(self.arr)):
            if self.arr[i] > large:
                large = self.arr[i]
        return large
    def find_small(self):
        small = self.arr[0]
        for i in range(1,len(self.arr)):
            if self.arr[i] < small:
                small = self.arr[i]
        return small
    def __str__(self):
        return "Largest number in the list is: "+ str(self.find_large())+ "\nSmallest number in the list is: "+ str(self.find_small())
    
if __name__ == "__main__":
    # arr = [10,20,30,40,50,200,60,70,80,90,100]
    n = int(input("Enter the number of elements in the list: "))
    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter the {i+1} element:  ")))
    print(f"\nList is: {arr}\n")
    print(large(arr))