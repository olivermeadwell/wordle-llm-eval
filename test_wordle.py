from wordle import score_guess, load_words


def test_exact_match_is_all_green():
    assert score_guess("CRANE", "CRANE") == "GGGGG"
def test_no_shared_letters_is_all_grey():
    assert score_guess("SLOTH", "CRANE") == "-----"
def test_mix_of_greens_and_yellows():
    assert score_guess("REACT", "CRANE") == "YYGY-"
def test_repeated_guess_letter_only_yellow_once():
    assert score_guess("SPEED", "ABIDE") == "--Y-Y"
def test_repeated_letter_can_be_green_and_yellow():
    assert score_guess("ROBOT", "FLOOR") == "YY-G-"
def test_green_uses_up_letter_before_yellows():
    assert score_guess("EERIE", "THERE") == "Y-Y-G"
def test_load_words_reads_every_answer():
    assert len(load_words("words/answers.txt")) == 1000
