class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def __str__(self):
        return f"BMI: {self.calculate_bmi()}"
    

if __name__ == "__main__":
    h=float(input("Enter your height in cm: "))
    w=float(input("Enter your weight in kg: "))
    BMI = BMI(w, h/100)
    print(BMI)
    if BMI.calculate_bmi()<18.5:
        print("You are underweight")
    elif BMI.calculate_bmi()>=18.5 and BMI.calculate_bmi()<25:
        print("You are weight is normal.")
    elif BMI.calculate_bmi()>=25 and BMI.calculate_bmi()<30:
        print("You are overweight.")
    else:
        print("You are obese.")