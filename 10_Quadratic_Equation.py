import math
def filter_float(x1,x2,none):
    if x1.is_integer():
        x1 = int(x1)
    if x2.is_integer():
        x2 = int(x2)
    if none ==1:
        print("Root 1: ", x1," ", x2, "i")
        print("Root 2: ", x1," ", -x2, "i")
    else:
        print("Roots are: ", x1," ", x2)


if __name__ == "__main__":
    print("Quadratic equation ax^2 + bx + c = 0")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    d = b**2 - 4*a*c
    if d < 0:
        print("Roots are imaginary!!")
        real = -b/(2*a)
        imaginary = math.sqrt(-d)/(2*a)
        filter_float(real,-imaginary,1)    
    elif d == 0:
        x = -b/(2*a)
        filter_float(x, x, 0)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        filter_float(x1, x2, 0)