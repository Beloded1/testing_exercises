import pytest

from functions.level_2.one_brackets import delete_remove_brackets_quotes


# Очевидно, что функция delete_remove_brackets_quotes реализована не совсем корректно, нужно было return name[1:len(name) - 1]
def test__delete_remove_brackets_quotes__if_get_string_with_brackets_return_string_without_brackets_and_without_some_letters():
    assert delete_remove_brackets_quotes("{Hello}") == "ell"


def test__delete_remove_brackets_quotes__if_get_string_without_brackets_return_the_same_string():
    assert delete_remove_brackets_quotes("World") == "World"


def test__delete_remove_brackets_quotes__if_get_empty_string_return_indexerror():
    with pytest.raises(IndexError):
        delete_remove_brackets_quotes("")


def test__delete_remove_brackets_quotes__get_string_with_additional_quotes_return_the_same_string():
    assert delete_remove_brackets_quotes("'World'") == "'World'"


def test__delete_remove_brackets_quotes__get_string_with_double_brackets_return_string_without_brackets():
    assert delete_remove_brackets_quotes("{{World}}") == "World"
