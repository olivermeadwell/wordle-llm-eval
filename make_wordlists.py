from wordfreq import top_n_list
from pathlib import Path


all_words = top_n_list("en", 50000)
allowed = [word.upper() for word in all_words if len(word) == 5 and word.isalpha() and word.isascii()]
answers = allowed[:1000]

Path("words").mkdir(exist_ok=True)
with open("words/allowed.txt", "w") as f:
    f.write("\n".join(allowed) + "\n")

with open("words/answers.txt", "w") as f:
    f.write("\n".join(answers) + "\n")

print(f"{len(allowed)} allowed words, {len(answers)} answers")
