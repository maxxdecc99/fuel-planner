import pytest

from targets import carbs_per_hour, sweat_rate


def test_carbs_short_race_needs_none():
    assert carbs_per_hour(30) == 0
    assert carbs_per_hour(44) == 0


def test_carbs_45_to_60_minutes():
    assert carbs_per_hour(45) == 20
    assert carbs_per_hour(59) == 20


def test_carbs_1_to_2_hours():
    assert carbs_per_hour(60) == 30
    assert carbs_per_hour(119) == 30


def test_carbs_2_to_2_5_hours():
    assert carbs_per_hour(120) == 60
    assert carbs_per_hour(149) == 60


def test_carbs_long_race():
    assert carbs_per_hour(150) == 90
    assert carbs_per_hour(600) == 90


def test_sweat_rate_one_hour():
    assert sweat_rate(70.0, 69.2, 300, 60) == 1100


def test_sweat_rate_ninety_minutes():
    assert sweat_rate(70.0, 69.2, 300, 90) == 733


def test_sweat_rate_rejects_zero_duration():
    with pytest.raises(ValueError):
        sweat_rate(70.0, 69.2, 300, 0)
