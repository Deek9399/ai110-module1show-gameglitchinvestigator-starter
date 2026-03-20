from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


# --- check_guess tests ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_winning_guess_message():
    outcome, message = check_guess(50, 50)
    assert "Correct" in message

def test_too_high_message_says_lower():
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_higher():
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_guess_at_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_guess_at_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"


# --- parse_guess tests ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err is not None

def test_parse_float_string():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5


# --- update_score tests ---

def test_win_on_first_attempt():
    # attempt_number=1 after increment: 100 - 10*(1+1) = 80
    score = update_score(0, "Win", 1)
    assert score == 80

def test_win_on_second_attempt():
    # attempt_number=2: 100 - 10*(2+1) = 70
    score = update_score(0, "Win", 2)
    assert score == 70

def test_win_score_minimum_floor():
    # High attempt number should not go below 10
    score = update_score(0, "Win", 20)
    assert score == 10

def test_too_high_deducts_score():
    score = update_score(50, "Too High", 1)
    assert score == 45

def test_too_low_deducts_score():
    score = update_score(50, "Too Low", 1)
    assert score == 45

def test_win_adds_to_existing_score():
    score = update_score(100, "Win", 1)
    assert score == 180


# --- get_range_for_difficulty tests ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_unknown_difficulty_defaults():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100
