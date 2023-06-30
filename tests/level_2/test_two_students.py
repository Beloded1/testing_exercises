import pytest

from functions.level_2.two_students import Student, get_student_by_tg_nickname


@pytest.mark.parametrize("telegram_username, expected_student", [
    ("AlexandrBeloded", Student("Alexandr", "Beloded", "@AlexandrBeloded")),
    ("OlegIvanov", Student("Oleg", "Ivanov", "@OlegIvanov")),
])
def test__get_student_by_tg_nickname__matching_username(telegram_username, expected_student):
    students = [
        Student("Alexandr", "Beloded", "@AlexandrBeloded"),
        Student("Oleg", "Ivanov", "@OlegIvanov"),
        Student("Denis", "Ivanov", None),
    ]

    assert get_student_by_tg_nickname(telegram_username, students) == expected_student


@pytest.mark.parametrize("telegram_username", [
    "non_user",
    "another_user",
])
def test__get_student_by_tg_nicknamenon__if_not_matching_username_return_none(telegram_username):
    students = [
        Student("Alexandr", "Beloded", "@AlexandrBeloded"),
        Student("Oleg", "Ivanov", "@OlegIvanov"),
        Student("Denis", "Ivanov", None),
    ]

    assert get_student_by_tg_nickname(telegram_username, students) is None
