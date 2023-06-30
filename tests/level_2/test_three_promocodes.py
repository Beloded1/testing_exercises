from unittest.mock import patch

import pytest

from functions.level_2.three_promocodes import generate_promocode


def test__generate_promocode__return_eight_symbols_with_default_promocode_len():
    with patch('random.choice') as random_choice_mock:
        random_choice_mock.return_value = 'Z'
        assert generate_promocode() == 'ZZZZZZZZ'


@pytest.mark.parametrize("promocode_len", [1, 5, 20])
def test__generate_promocode__get_different_promocode_with_some_lenght_return_promocode_with_the_same_promocode_lenght(promocode_len):
    assert len(generate_promocode(promocode_len)) == promocode_len


@pytest.mark.parametrize("promocode_len", [1, 10, 100])
def test__generate_promocode__get_promocode_with_different_lenght_return_unique_promocode(promocode_len):
    promocode1 = generate_promocode(promocode_len)
    promocode2 = generate_promocode(promocode_len)
    assert promocode1 != promocode2
