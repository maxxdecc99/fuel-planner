from schedule import gel_interval_minutes


def test_gel_interval_exact_fit():
    assert gel_interval_minutes(25, 60) == 25


def test_gel_interval_rounds_down_to_5():
    assert gel_interval_minutes(25, 90) == 15
    assert gel_interval_minutes(22, 60) == 20
