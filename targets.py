def carbs_per_hour(duration_minutes: int) -> int:
    if duration_minutes < 45:
        return 0
    elif duration_minutes < 60:
        return 20
    elif duration_minutes < 120:
        return 30
    elif duration_minutes < 150:
        return 60
    else:
        return 90

assert carbs_per_hour(44) == 0
assert carbs_per_hour(45) == 20
assert carbs_per_hour(59) == 20
assert carbs_per_hour(60) == 30
assert carbs_per_hour(70) == 30
assert carbs_per_hour(130) == 60
assert carbs_per_hour(160) == 90
assert carbs_per_hour(119) == 30
assert carbs_per_hour(120) == 60
assert carbs_per_hour(149) == 60
assert carbs_per_hour(150) == 90
print("all carbs per hour tests work")


def sweat_rate(weight_before_kg: float, weight_after_kg: float, fluid_drunk_ml: int, duration_minutes: int) -> int:
    return round(((weight_before_kg - weight_after_kg) * 1000 + fluid_drunk_ml) / (duration_minutes / 60))

assert sweat_rate(70.0, 69.2, 300, 60) == 1100
assert sweat_rate(70.0, 69.2, 300, 90) == 733
print("all sweat rate tests work")
