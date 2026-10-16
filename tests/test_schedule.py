from schedule import carbs_from_gels_per_hour, gel_interval_minutes


def test_gel_interval_exact_fit():
    assert gel_interval_minutes(25, 60) == 25


def test_gel_interval_rounds_down_to_5():
    assert gel_interval_minutes(25, 90) == 15
    assert gel_interval_minutes(22, 60) == 20


def test_no_gels_needed_when_drink_covers_carbs():
    assert gel_interval_minutes(25, 0) is None

def test_gels_cover_everything_with_water():
    assert carbs_from_gels_per_hour(60, 500, 0) == 60


def test_drink_covers_part_of_carbs():
    assert carbs_from_gels_per_hour(60, 500, 60) == 30


def test_gels_never_negative():
    assert carbs_from_gels_per_hour(30, 600, 60) == 0


def test_drink_covering_everything_means_no_gels():
    gels = carbs_from_gels_per_hour(30, 600, 60)
    assert gel_interval_minutes(25, gels) is None
