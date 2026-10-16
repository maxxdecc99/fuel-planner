def gel_interval_minutes(carbs_per_gel: int, carbs_from_gels_per_hour: int) -> int | None:
    if carbs_from_gels_per_hour <= 0:
        return None
    carbs_per_minute = carbs_from_gels_per_hour / 60
    exact_minutes_per_gel = carbs_per_gel / carbs_per_minute
    blocks_of_5 = exact_minutes_per_gel // 5
    return int(blocks_of_5 * 5)


def carbs_from_gels_per_hour(carbs_target_per_hour: int, fluid_ml_per_hour: int, drink_carbs_per_liter: int) -> int:
    fluid_liter_per_hour = fluid_ml_per_hour / 1000
    carbs_from_drink = fluid_liter_per_hour * drink_carbs_per_liter
    carbs_from_gels = carbs_target_per_hour - carbs_from_drink
    return round(max(0, carbs_from_gels))

print(carbs_from_gels_per_hour(60, 500, 0))
print(carbs_from_gels_per_hour(60, 500, 60))
print(carbs_from_gels_per_hour(30, 600, 60))
