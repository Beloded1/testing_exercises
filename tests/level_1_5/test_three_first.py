from functions.level_1_5.three_first import first
import pytest


@pytest.mark.parametrize(
        'items, default, expected_result',
    [
        ([5, 7, 1, 15], None, 5),
        ([1, 2, 4, 1], None, 1),
        ([7, 14, 1, 28], None, 7),
        ([1, 1, 1, 1], None, 1),
        ([1, 0, 0, 0], None, 1),
        ([0, 0, 0, 0], None, 0),
        ([-10, 0, 0, 0], None, -10),
        ([-10, -20, -50, -100], None, -10),
    ]
)
def test__first__return_first_item_if_items_is_not_empty(items, default, expected_result):
    assert first(items, default) == expected_result


def test__first__raise_error_if_empty_items_and_default_are_not_set():
    with pytest.raises(AttributeError):
        first([])


def test__first__return_none_if_empty_items_found_and_default_is_none():
    assert first([], None) == None


def test__first__return_default_if_empty_items_found_and_default_is_int():
    assert first([], 0) == 0

@pytest.mark.parametrize(
    'items, default, expected_result',
    [
        ([5, 7, 1, 15], None, 5),
        ([], None, None),
        ([], 0, 0),
    ],
    ids=[
        'return_first_item_if_items_is_not_empty',
        'return_none_if_empty_items_found_and_default_is_non',
        'return_default_if_empty_items_found_and_default_is_int'
    ]
)
def test__first(items, default, expected_result):
    assert first(items, default) == expected_result