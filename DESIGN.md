# Design: race fuel planner

## Scenario

A runner is preparing for a race. They know the distance, maybe their expected
finish time, and what they plan to carry. Often they don't know how much to eat
and drink. The tool tells them what to take, when, and how much, and turns that
into a plan they can follow while running.

The plan succeeds when it:
- meets the runner's targets for carbs, fluid and sodium, or comes as close as their gear allows
- fits what the runner can carry
- is simple enough to follow during a race

## Principles

1. **The more you enter, the more specific the plan.** Measured beats entered, entered beats estimated.
2. **No invented advice.** Estimates come from published guidelines. Where the tool makes its own assumption, it says so.
3. **A plan you can follow beats an exact plan you can't.** Times are rounded to 5 minutes.
4. **When in doubt, more rather than less.** Boundaries round up, and the packing list includes a reserve.
5. **Show the gap.** If the runner's gear can't meet the recommendation, the plan says so and suggests a fix.

## Versions

| Version | Adds |
|---|---|
| v1 | Distance, time, targets, flasks, gels, aid stations → plan |
| v2 | Product file with brands, fueling strategy, caffeine with a total limit |
| v3 | GPX input and elevation |
| v4 | Profiles, tests, packaging |

## Input (v1)

| Input | Required | If missing |
|---|---|---|
| Distance (km) | yes | — |
| Expected time, or a range | no | average finish time for the distance |
| Reserve (%) | no | 15% |
| Carb target (g/h) | no | estimated from duration |
| Fluid target (ml/h) | no | sweat test → estimated from temperature and sweat profile |
| Temperature (°C or °F) | no | needed only for the fluid estimate |
| Sweat profile: little / average / a lot | no | average |
| Salty sweater: yes / no / don't know | no | don't know |
| Flasks: count, volume, contents (water, or drink with carbs and sodium per liter) | no | — |
| Gels: carbs and sodium per gel, max carried | no | — |
| Aid stations: km, water and/or sports drink | no | — |

## Output

1. **Assumptions** — what the plan is based on, and which values were estimated
2. **Targets per hour** — carbs, fluid, sodium, with their source
3. **Gel schedule** — time and km
4. **Drink schedule** — sips, refills and cups at aid stations
5. **Packing list** — including the reserve
6. **Warnings** — gaps between recommendation and plan, with a suggestion

## Rules

### Carbs per hour (estimated)

| Duration | Carbs |
|---|---|
| < 45 min | 0 g |
| ≥ 45 min and < 60 min | 20 g |
| ≥ 60 min and < 2 h | 30 g |
| ≥ 2 h and < 2.5 h | 60 g |
| ≥ 2.5 h | 90 g |

Based on Jeukendrup (2014). Exactly on a boundary goes to the higher group.
Estimated targets are capped at 90 g/h. User-entered targets are not capped,
but anything above 90 g/h shows a warning.

### Fluid per hour

Priority: sweat test → user-entered → estimated.

**Sweat test:**
`sweat rate (ml/h) = ((weight before − weight after) × 1000 + fluid drunk in ml) ÷ duration in hours`

**Estimate:**
- base: 400 ml/h at ≤ 10 °C, 800 ml/h at ≥ 25 °C, linear in between
- sweat profile: little −100 ml, average ±0, a lot +100 ml
- result is always clamped to 400–800 ml/h

The 400–800 ml/h range is from the ACSM (2007). The temperature boundaries and the
±100 ml adjustment are own assumptions.

### Sodium

Per liter of fluid, so more fluid means more sodium.

| Salty sweater | Sodium per liter |
|---|---|
| yes | 690 mg |
| don't know | 575 mg |
| no | 460 mg |

Based on the 20–30 mmol/L range used in sports drink research.
Product labels in the EU often list salt instead of sodium: `sodium (mg) = salt (g) × 400`.

### Gel schedule

```
carbs from drink = fluid target (L/h) × carbs per liter of drink
carbs from gels  = carb target − carbs from drink
interval (min)   = carbs per gel ÷ carbs from gels × 60
```

Rounded **down** to 5 minutes. If that pushes an estimated target above 90 g/h,
round **up** instead and show a warning.

If the drink already covers the carb target, no gels are needed.

### Drink schedule

- Sips at a fixed interval
- A flask is emptied over each segment between refills
- One cup at an aid station = 150 ml (own assumption, configurable)
- Calculated **per segment**, not only as a total

### Shortfalls

If a segment falls below the lower guideline (400 ml/h for fluid), the plan shows a
warning with a suggestion, for example an extra cup at the next aid station or a
second flask. The tool does not change the plan on its own.

## Validation

| Input | Allowed | Check |
|---|---|---|
| Distance | 1–1000 km | range |
| Expected time | > 0 | range |
| Pace (derived) | 2:30–20:00 min/km | consistency |
| Temperature | −20–50 °C | range |
| Gel carbs | 1–100 g | range |
| Flask volume | 50–2000 ml | range |
| Aid station | > 0, < distance, ascending | consistency |
| Reserve | 0–100% | range |

Error messages say what is wrong and how to fix it.

## Known limitations

- Multi-day races: the per-hour model doesn't account for sleep or real meals.
- Estimates are general guidelines, not personal advice.

## Open questions

- Average finish times per distance: find a source.
- Schedule shows both time and km, or one of them?

## Sources

- Jeukendrup, A. (2014). A step towards personalized sports nutrition: carbohydrate intake during exercise. *Sports Medicine* 44 (Suppl 1), 25–33.
- American College of Sports Medicine (2007). Exercise and fluid replacement. *Medicine & Science in Sports & Exercise* 39(2), 377–390.
