from functions.level_1.two_date_parser import compose_datetime_from
import datetime, pytest
from freezegun import freeze_time


@freeze_time("2023-06-01 12:00:00")
def test__compose_datetime__from_today():
    result = compose_datetime_from("today", "10:30")
    expected_result = datetime.datetime(2023, 6, 1, 10, 30)
    assert result == expected_result


@freeze_time("2023-06-01 12:00:00")
def test__compose_datetime__from_tomorrow():
    result = compose_datetime_from("tomorrow", "14:45")
    expected_result = datetime.datetime(2023, 6, 2, 14, 45)
    assert result == expected_result


def test__compose_datetime__wrong_time_format():
    with pytest.raises(ValueError):
        compose_datetime_from("today", "10-30")
