# bot_player.py
from game_module import play_game

# Let bot choose easy mode and make random guesses up to 100
def bot_input_generator():
    inputs = ["easy"]  # First input: difficulty
    inputs.extend(str(i) for i in range(1, 101))  # Next guesses: 1 to 100
    for item in inputs:
        yield item

gen = bot_input_generator()

def bot_input(prompt):
    value = next(gen)
    print(f"{prompt}{value}")  # Shows what the bot inputs
    return value

play_game(bot_input)
