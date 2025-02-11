import random
RandNumb = random.randint(1,100)
# It will take a random intager value from 1- 100
print("!!______xx___Guess a number between 1 to 100 ____xx____!!")
User = int(input("Enter your guess: "))
while 1:
    if User > 100 or User < 1:
        print("Please enter a number between 1 to 100 !")
        User = int(input("Enter your guess: "))
    elif User < RandNumb:
        print("Guess a higher number! ")
        User = int(input("Enter your guess: "))
    elif User > RandNumb:
        print("Guess a lower number! ")
        User = int(input("Enter your guess: "))
    else:
        print("!!______xx___Congratulation! You have guessed the correct number!____xx____!!")
        break
