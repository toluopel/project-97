import random 
print ("Number Guessing Game")
number = random.randint
number = 6
chances = 0
print("Guess a number (between 1 and 9): ")

while chances < 5:

    guess = int(input("Enter your guess: "))


    if guess == number:
        print("Congrats, YOU WON!!!")
        break

    elif guess < number:
        print("Your number was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)    

    chances == 1

    if not chances < 5:
        print("YOU LOSE!!! The number is", number)    
