import replit
import random
from words import *
from art import *

print(logo)
random_word = random.choice(lst).lower()
word_length = len(random_word)
lives = 6
display = ['_' for _ in range(word_length)]
print(display)
# print(random_word)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    replit.clear()
    if guess in display:
        print("You've already guesses this letter")

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            print("You Lose")
            end_of_game = True
    if '_' not in display and lives > 0:
        print("You Win")
        end_of_game = True
    print(stages[lives])
