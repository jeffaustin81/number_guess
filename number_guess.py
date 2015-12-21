import random
import sys

def guess_my_number():
    secret_number = random.randint(1,10)
    i = 0
    while i < 5:
        try:
            guess = int(input("Guess a number between 1 and 10, you get five guesses: "))
            i += 1
            if guess > secret_number:
                print("Guess {}".format(i))
                print("Too high!")
            elif guess < secret_number:
                print("Guess {}".format(i))
                print("Too low!")
            elif guess == secret_number:
                print("Guess {}".format(i))
                print("You got it! The secret number was {}".format(secret_number))
                break
        except ValueError:
            print("That was not a number!")

    again = input("Would you like to play again? Y/n: ")

    if again.lower() != "n":
        guess_my_number()
    else:
        sys.exit("Bye!")

guess_my_number()



