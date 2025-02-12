import math
if __name__ == "__main__":
    a = int(input("Enter lower number: "))
    b = int(input("Enter upper number: "))
    primevalue = []
    print("Prime numbers between", a, "and", b, "are:")
    for i in range(a,b+1):
        if i>1:
            for j in range(2,int(math.sqrt(i))+1):
                if i%j == 0:
                    break
            else:
                primevalue.append(i)
    print("Total found: ", len(primevalue))
    print(primevalue)