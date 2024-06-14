"""
Engeto-project-Bulls&Cows.py: - 2nd Engeto project - Bulls & Cows
author: Lukáš Vavrčík
email: lukasvavrcik@gmail.com
discord: lukardi.
"""

import random
#game definitons

# separator definition
separator = "-" * 60

# welcome text definition
welcome_text = print(f"Hi there!", separator,
                "I've generated a random 4 digit number for you.",
                "Let's play a bulls and cows game.",
                separator,
                "Enter a number:",
                separator, sep="\n")

# random four digits number generator
def random_number():
    number = str(random.randint(1000, 9999))
    while len(number) != len(set(number)):
        number = str(random.randint(1000, 9999))
    return number

# player's input & check of compliance with the rules
'''
Rules of the game:
    Player can't:
    - input less/more than exact 4 numbers (four-digit number)
    - input number with duplicities
    - input number starts with O (zero)
    - input anything else than digits
'''

def players_input_check(input):
    if len(input) != 4 or not input.isdigit():
        print(f"Sorry, this is not a four-digit number. Try again!", separator, sep="\n")
        return False
    elif len(input) != len(set(input)):
        print(f"Sorry, you can't input same digit twice. Try again!", separator, sep="\n")
        return False
    elif input[0] == "0":
        print(f"Number you're entering can't start with zero. Try again!", separator, sep="\n")
        return False
    else:
        return True

# calculation based on player's input
def bulls_and_cows_count(random_number, guess):
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        if random_number[i] == digit:
            bulls += 1
        elif digit in random_number:
            cows += 1
    return bulls, cows

# calculation - number of attempts
def scorecard(number_of_attempts):
    if number_of_attempts <= 5:
        print(f"Wow, amazing!")
    elif number_of_attempts <= 10:
        print(f"Very good score!")
    elif number_of_attempts <= 15:
        print(f"Not too bad.")
    elif number_of_attempts <= 20:
        print(f"Not so good.")
    else:
        print(f"Eh - time to practice.")

# game
def game():
    # welcome the  player
    welcome_text
    # generate random number
    number = random_number()

    attempts = 0

    # player's input
    while True:
        guess = input(">>> ")

        attempts += 1

        if players_input_check(guess):
            if guess == number:
                print(f"Correct, you've guessed the right number in {attempts} guesses!")
                break
            else:
                bulls, cows = bulls_and_cows_count(number, guess)
                if bulls == 1 and cows == 1:
                    print(f"{bulls} bull and {cows} cow")
                elif bulls == 1:
                    print(f"{bulls} bull and {cows} cows")
                elif cows == 1:
                    print(f"{bulls} bulls and {cows} cow")
                else:
                    print(f"{bulls} bulls and {cows} cows")
            print(separator)

    print(separator)
    scorecard(attempts)


if __name__ == "__main__":
    game()