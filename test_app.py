import pytest
from app import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 1000)

def test_hard_harder_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

def test_unknown_difficulty_defaults_to_normal():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess ---

def test_parse_guess_none():
    ok, val, err = parse_guess(None)
    assert ok is False
    assert val is None
    assert err == "Enter a guess."

def test_parse_guess_empty():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None

def test_parse_guess_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None

def test_parse_guess_float_string():
    ok, val, err = parse_guess("7.9")
    assert ok is True
    assert val == 7

def test_parse_guess_non_numeric():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert val is None
    assert err == "That is not a number."

def test_parse_guess_negative():
    ok, val, err = parse_guess("-5")
    assert ok is True
    assert val == -5


# --- check_guess ---

def test_check_guess_correct():
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in msg

def test_check_guess_too_high():
    outcome, msg = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in msg

def test_check_guess_too_low():
    outcome, msg = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in msg

def test_check_guess_one_below():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

def test_check_guess_one_above():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"


# --- update_score ---

def test_update_score_win_first_attempt():
    # attempt_number=1: 100 - 10*1 = 90
    score = update_score(0, "Win", 1)
    assert score == 90

def test_update_score_win_enforces_minimum():
    # attempt_number=10: 100 - 10*10 = 0, clamped to 10
    score = update_score(0, "Win", 10)
    assert score == 10

def test_update_score_too_high_deducts():
    score = update_score(50, "Too High", 1)
    assert score == 45

def test_update_score_too_low_deducts():
    score = update_score(50, "Too Low", 1)
    assert score == 45

def test_update_score_win_adds_to_existing():
    score = update_score(100, "Win", 1)
    assert score == 190

def test_update_score_unknown_outcome_unchanged():
    score = update_score(50, "SomeOtherOutcome", 1)
    assert score == 50
