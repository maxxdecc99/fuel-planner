def gel_interval_minutes(carbs_per_gel: int, carbs_from_gels_per_hour: int) -> int:
    carbs_per_minute = carbs_from_gels_per_hour / 60
    exact_minutes_per_gel = carbs_per_gel / carbs_per_minute
    blocks_of_5 = exact_minutes_per_gel // 5
    return int(blocks_of_5 * 5)
