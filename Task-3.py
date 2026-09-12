import math

backend_variants = math.comb(8, 2)
frontend_variants = math.comb(6, 2)
designer_variants = math.comb(4, 1)

total_teams = (
    backend_variants
    * frontend_variants
    * designer_variants
)

print(
    f"Способів вибрати 2 Back-end розробників із 8: "
    f"{backend_variants}"
)

print(
    f"Способів вибрати 2 Front-end розробників із 6: "
    f"{frontend_variants}"
)

print(
    f"Способів вибрати 1 дизайнера з 4: "
    f"{designer_variants}"
)

print(f"\nЗагальна кількість можливих команд: {total_teams}")