import random

guessestaken = 0

myname = input("Hello, what is your name?  ")

number = random.randint(1, 20)
print("Hello, " + myname + ", I am thinking of a number between 1 and 20.")

for guessestaken in range(6):
    guess = input("Please take a guess.  ")
    guessednumber = int(guess)

    if guessednumber > number:
        print("I am sorry.  Your number is too high")
    if guessednumber < number:
        print("I am sorry.  Your number is too low")
    if guessednumber == number:
        break

if guessednumber == number:
    guessestaken = str(guessestaken + 1)
    print("Good work!  You guessed the number in " + guessestaken + " guesses!")
if guessednumber != number:
    number = str(number)
    print("I am sorry, " + myname + ", my number was " + number + ".  Hope that you win next time!")