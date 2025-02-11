num1 = int(input("Enter first number: "))
num2 = int(input('Enter second number: ')) 
mult = num1 * num2
print("Result of {} * {} is:  {}".format(num1,num2,mult))
if num2 ==0:
    print("Division by zero is not possible")
else:
    div = num1/num2
    print("Result of",num1,"/",num2,"is: ",div)