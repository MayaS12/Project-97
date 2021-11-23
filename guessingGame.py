import random;

number = random.randint(0,9)

print("Guess a number from 0-9:")

chances = 0

while chances < 5:
    guessNumber = int(input("Enter your guess:"))
    if number == guessNumber:
        print("YOU WON!!!")
        break
    elif guessNumber > number:
        print("That's too high! Try a little lower")
    elif guessNumber < number:
        print("That's too low. Try a little higher")
    chances = chances+1

if not chances < 5:
    print("You lose! The number is:", number)
