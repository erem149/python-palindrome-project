# While Loops
print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

i=0
while i < 5:
    # print(f"{i+1}." + '*' * (i+1) + "Loops are awesome" + '*' * (i+1))
    # i=i+1 # starting with 1
    i+=1 # starting with 1
    print(f"{i}." + '*' * i + "Loops are awesome" + '*' * i)
    # i=i+1 -> starting with 0
    
# While Loops - Exercise
print('Guessing game')
# Gues the correct number in 3 guesses. If you don't get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins, 2. If user loses
# Tip:( remember you won't see print statements during execution, so If you want to see prints during while loop, then print to the input box )
# This is specific to this platform)
# while condition:
#     code
#     iterator
# Three Loop Questions:
#1. What do I want to repeat?
# -> guesses
#2. What do I want to change each time?
# -> guess number and number of guesses
#3. How long should we repeat?
# -> until user loses, runs out of guesses, or wins

secret_num = 12
guess = 0
guess_limit = 3
guess_number = 0

while guess_number < guess_limit:
    guess = int(input(f"Guess #{guess_number+1} a number 1-20 (last guess: {guess}): "))
    if guess == secret_num:
        print(f"You Win! You Guessed it: {guess}")
        break
    else:
        print(f"No, not {guess}!")
        guess_number += 1
if guess != secret_num:
    print(f"Sorry you Lose! It was {secret_num}")
#Modification Version
#Modification 1: number 1-100, tell user if guess is too high/low, and let them have 5-10 guesses.
# Tip: ( remember you won't see print statements during execution, so If you want to see prints during while loop, print to the input box 
secret_num = 76
guess = 0
guess_limit = 5
guess_number = 0
guess = int(input(f"Guess a number 1-100: "))
guess_number += 1
while guess_number < guess_limit:
    if guess != secret_num:
        guess_number += 1
        if guess > secret_num:
            guess = int(input(f"{guess} Too high - Guess again 1-100: "))
        else:
            guess = int(input(f"{guess} Too low - Guess again 1-100: "))
    if guess == secret_num:
        print(f"You Win! You Guessed it: {guess}")
        break
if guess != secret_num:
    print(f"Sorry you Lose! It was {secret_num}")