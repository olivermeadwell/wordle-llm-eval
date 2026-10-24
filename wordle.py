from collections import Counter


def score_guess(guess: str, answer: str) -> str:
    """Score a guess against the answer. G = right spot, Y = wrong spot, - = not in word."""
    marks = ["-"] * 5
    available = Counter()
    for i in range(5):
        if guess[i] == answer[i]:
            marks[i] = "G"
        else:
            available[answer[i]] += 1
    for i in range(5):
        if marks[i] != "G" and available[guess[i]] > 0:
                marks[i] = "Y"
                available[guess[i]] -= 1
    return "".join(marks)
