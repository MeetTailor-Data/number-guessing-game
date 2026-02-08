import random

num = random.randint(1, 100)
no_of_guess = 0

while True:
    guessed_number = int(input("Guess a Number Between 1 to 100: "))
    no_of_guess += 1

    if guessed_number > num:
        print("Your Guess is High")
    elif guessed_number < num:
        print("Your Guess is Low")
    else:
        print("Congrats!! You guessed it right ")
        break

print("Number of Guesses:", no_of_guess)
