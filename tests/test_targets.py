import pytest

from targets import base_fluid_per_hour, carbs_per_hour, sweat_rate, estimated_fluid_per_hour, sodium_per_liter, sodium_per_hour


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

def test_base_fluid_cold_is_minimum():
    assert base_fluid_per_hour(5) == 400
    assert base_fluid_per_hour(10) == 400


def test_base_fluid_hot_is_maximum():
    assert base_fluid_per_hour(25) == 800
    assert base_fluid_per_hour(30) == 800


def test_base_fluid_in_between():
    assert base_fluid_per_hour(16) == 560
    assert base_fluid_per_hour(17.5) == 600

def test_estimated_fluid_by_profile():
    assert estimated_fluid_per_hour(16, "low") == 460
    assert estimated_fluid_per_hour(16, "average") == 560
    assert estimated_fluid_per_hour(16, "high") == 660


def test_estimated_fluid_never_below_minimum():
    assert estimated_fluid_per_hour(8, "low") == 400


def test_estimated_fluid_never_above_maximum():
    assert estimated_fluid_per_hour(30, "high") == 800


def test_estimated_fluid_rejects_unknown_profile():
    with pytest.raises(ValueError):
        estimated_fluid_per_hour(16, "medium")

def test_sodium_per_liter_by_profile():
    assert sodium_per_liter("yes") == 690
    assert sodium_per_liter("unknown") == 575
    assert sodium_per_liter("no") == 460


def test_sodium_per_liter_rejects_unknown_answer():
    with pytest.raises(ValueError):
        sodium_per_liter("maybe")


def test_sodium_per_hour():
    assert sodium_per_hour(600, "yes") == 414
    assert sodium_per_hour(500, "no") == 230
