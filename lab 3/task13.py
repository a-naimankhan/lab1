import random

def guess_a_number(name, random_number):
    counter = 0
    while True:
        counter += 1
        num = int(input()) 
        if num == random_number:
            print(f"Good job, {name}! You guessed my number in {counter} guesses!")
            break
        elif num < random_number:
            print("Your guess is too low.\nTake a guess.")
        else:
            print("Your guess is too high.\nTake a guess.")

print("Hello, what is your name?")
name = input()
random_number = random.randint(1, 100)
guess_a_number(name, random_number)
