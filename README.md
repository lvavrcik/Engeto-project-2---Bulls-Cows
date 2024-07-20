# Engeto-project-2---Bulls&Cows
Code for 2nd Engeto project - Bulls&Cows game

**Čeština:**  
> [Přečtěte si českou verzi README](README_cs.md)


# Bulls & Cows game #
## Project description ##
Aim of this project is to create a program simulating the Bulls & Cows game.
Player has to decode a secret four-digit number.

**Program description**: 
- program greets the user and displays introductory text
- program creates a secret four-digit number (numbers has to be unique and must not start with 0)
- player guesses the number. Program will alert the player if:
    - player enters a number shorter/longer than 4 digits
    - number contains duplicates
    - number starts with a zero
    - number contains non-numeric characters

- program evaluates player's guess
- program will also display the number of bull/bulls (if user guessed right both the number and its location), or cow/cows (if user guessed only the correct number but not its location). Returned evaluation must take into account the singular and plural in the output - so 1 bull and 2 bulls (same for cow/cows).
- once the player has guessed the number, program congratules the player and terminates

- program also counts total number of the player's attempts + evaluates the player's game based on the number of attempts

**Values on a scale**:
- number of attempts <= 5 - Wow, amazing
- number of attempts <= 10 - Very good score
- number of attempts <= 15 - Not too bad
- number of attempts <= 20 - Not so good
- number of attempts > 20 - Time to practice