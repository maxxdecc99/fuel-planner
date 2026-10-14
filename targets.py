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


def sweat_rate(weight_before_kg: float, weight_after_kg: float, fluid_drunk_ml: int, duration_minutes: int) -> int:
    if duration_minutes <= 0:
        raise ValueError(f"Duration must be more than 0 minutes, got {duration_minutes}")
    weight_loss_ml = (weight_before_kg - weight_after_kg) * 1000
    total_sweat_ml = weight_loss_ml + fluid_drunk_ml
    duration_hours = duration_minutes / 60
    return round(total_sweat_ml / duration_hours)


def base_fluid_per_hour(temperature_c: float) -> int:
    ml_per_degree = 400 / (25 - 10)
    degrees_above_10 = temperature_c - 10
    if temperature_c <= 10:
        return 400
    elif temperature_c >= 25:
        return 800
    else:
        return round(400 + ml_per_degree * degrees_above_10)
