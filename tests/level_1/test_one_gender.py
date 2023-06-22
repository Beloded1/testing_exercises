from functions.level_1.one_gender import genderalize
import pytest


@pytest.mark.parametrize(
        'verb_male, verb_female, gender, expected_result',
    [
        ('говорил', 'говорила', 'male', 'говорил'),
        ('кричал', 'кричала', 'male', 'кричал'),
        ('кукорекал', 'кукорекала', 'male', 'кукорекал'),
    ]
)
def test__genderalize__is_male(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result


@pytest.mark.parametrize(
        'verb_male, verb_female, gender, expected_result',
    [
        ('говорил', 'говорила', 'female', 'говорила'),
        ('кричал', 'кричала', 'transgender', 'кричала'),
        ('кукорекал', 'кукорекала', 'any str, except "male"', 'кукорекала'),
    ]
)
def test__genderalize__where_gender_is_not_male(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result
