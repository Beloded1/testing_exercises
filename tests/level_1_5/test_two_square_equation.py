import pytest

from functions.level_1_5.two_square_equation import solve_square_equation


def test__solve_square_equation__return_none_if_discriminant_is_negative():
    assert solve_square_equation(1.0, 1.0, 1.0) == (None, None)


def test__solve_square_equation__return_two_roots_if_discriminant_is_positive():
    assert solve_square_equation(1.0, -3.0, 2.0) == (1.0, 2.0)


@pytest.mark.xfail
def test__solve_square_equation__return_one_root_if_discriminant_is_equal_to_zero():
    assert solve_square_equation(1.0, -2.0, 1.0) == (1, None)


def test__solve_square_equation__return_one_root_if_square_coefficient_is_equal_to_zero():
    assert solve_square_equation(0, 2.0, 1) == (-0.5, None)


def test__solve_square_equation__return_none_if_square_coefficient_and__linear_coefficients_are_equal_to_zero():
    assert solve_square_equation(0, 0, 1) == (None, None)

@pytest.mark.parametrize(
    'square_coefficient, linear_coefficient, const_coefficient, expected_result',
    [
        (1.0, 1.0, 1.0, (None, None)),
        (1.0, -3.0, 2.0, (1.0, 2.0)),
        (1.0, -2.0, 1.0, (1, 1)),
        (0, 0, 1, (None, None)),
    ]
)
def test__solve_square_equation(square_coefficient, linear_coefficient, const_coefficient, expected_result):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_result