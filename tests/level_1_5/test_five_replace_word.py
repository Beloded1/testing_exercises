from functions.level_1_5.five_replace_word import replace_word
import pytest

def test__replace_word__starts_with_case_irrelevant():
    assert replace_word('the big black car', 'big', 'Cool') == 'the Cool black car'


@pytest.mark.parametrize(
    'text, replace_from, replace_to, expected_result',
    [
        ('the big black car', 'small', 'Cool', 'the big black car'),
        ('the big black car', 'white', 'small', 'the big black car'),
        ('the BIG black car', 'STRONG', 'cool', 'the BIG black car'),
    ]
)
def test__replace_word__unchanged_when_replace_word_not_found_in_text(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(
    'text, replace_from, replace_to, expected_result',
    [
        ('the big black car', 'big', 'Cool', 'the Cool black car'),
        ('the big black car', 'red', 'small', 'the big black car'),
        ('the BIG black car', 'big', 'cool', 'the cool black car'),
        ('the big black car', 'big', 'COOL', 'the COOL black car'),
        ('the big black car', 'BIG', 'cool', 'the cool black car'),
    ]
)
def test__replace_word(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result