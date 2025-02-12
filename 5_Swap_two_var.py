a =input("Enter first value ")
b = input("Enter second value ")
print(f"Orginal value 1 =  {a}  and value 2 =  {b} .")
# swap useing third variable
temp= a
a = b
b = temp
print(f"After swap value 1 =  {a}  and value 2 =  {b} .")


# swap without using third variable
a,b = b,a
print(f"Again swap Back to orginal value 1 =  {a}  and value 2 =  {b} .")