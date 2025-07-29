# game_module.py
import random

def play_game(get_input):
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)

    difficulty = get_input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty != 'hard' else 5

    def check_guess(guess):
        if guess > secret_number:
            print("Too high.")
            return False
        elif guess < secret_number:
            print("Too low.")
            return False
        else:
            print(f"🎉 Correct! The number was {secret_number}")
            return True

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        try:
            guess = int(get_input("Make a guess: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if check_guess(guess):
            return True
        attempts -= 1

    print(f"\n😢 You've run out of guesses. The number was {secret_number}.")
    return False
