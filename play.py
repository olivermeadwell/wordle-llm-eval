import random

from wordle import to_emoji, load_words, score_guess

ALLOWED = set(load_words("words/allowed.txt"))
POSSIBLE_ANSWERS = load_words("words/answers.txt")
MAX_TURNS = 6

answer = random.choice(POSSIBLE_ANSWERS)
turn = 1

print("Guess the word")
while turn <= MAX_TURNS:
    guess = input(f"Guess {turn}/{MAX_TURNS}: ").strip().upper()
    if guess not in ALLOWED:
        print("Not in the word list")
        continue
    print(guess, to_emoji(score_guess(guess, answer)))
    if guess == answer:
        print(f"Solved in {turn}")
        break
    turn += 1
else:
    print(f"Ran out of turns. The word was {answer}")
