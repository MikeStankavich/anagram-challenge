from anagram import Anagram

import pytest


ANAGRAM_DICTIONARY = {3: {"DGO": ["DOG", "GOD"]}, 4: {"EEKW":["WEEK", "KEEW"]}}
DIFFICULTY = "3"

@pytest.fixture(scope='session')
def anagram():
    anagram = Anagram(difficulty=DIFFICULTY, unsolvable=False, anagram_dictionary=ANAGRAM_DICTIONARY)
    return anagram


@pytest.fixture(scope='session')
def unsolvable_anagram():
    anagram = Anagram(difficulty=DIFFICULTY, unsolvable=True, anagram_dictionary=ANAGRAM_DICTIONARY)
    return anagram


def test_load_anagram_dictionary(anagram):
    words = anagram.anagram_dictionary
    assert words is not None
    assert isinstance(words, dict)
    assert isinstance(words.get(3), dict)


def test_get_puzzle(anagram):
    puzzle = anagram.generate_anagram_puzzle()
    assert len(puzzle) == DIFFICULTY


def test_generate_puzzle(anagram):
    user_answer = "dog"
    puzzle = anagram.generate_anagram_puzzle()
    answers = anagram.get_puzzle_answers()
    assert puzzle != user_answer
    assert anagram.is_anagram(user_answer) is True
    assert user_answer.upper() in answers
    assert sorted(puzzle) == sorted(user_answer.upper())
    assert len(puzzle) == len(user_answer)


def test_generate_unsolvable_puzzle(unsolvable_anagram):
    answers = unsolvable_anagram.get_puzzle_answers()
    puzzle = unsolvable_anagram.generate_unsolvable_puzzle()
    assert puzzle not in answers
    

def test_is_anagram(anagram):
    user_answer = "dog"
    assert anagram.is_anagram(user_answer) is True
    user_answer = "DOG"
    assert anagram.is_anagram(user_answer) is True
    user_answer = "odg"
    assert anagram.is_anagram(user_answer) is False
