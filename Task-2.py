from itertools import product


def check_access(
    is_employee,
    is_verified,
    is_premium,
    is_admin,
    is_banned
):
    base_access = (
        is_employee
        and is_verified
        and not is_banned
    )

    premium_access = (
        (is_employee or is_premium)
        and is_verified
        and not is_banned
    )

    admin_access = (
        is_admin
        and is_verified
        and not is_banned
    )

    secret_access = (
        (is_admin or (is_employee and is_premium))
        and is_verified
        and not is_banned
    )

    return {
        "Base": base_access,
        "Premium": premium_access,
        "Admin": admin_access,
        "Secret": secret_access
    }


# Генеруємо всі 2^5 = 32 комбінації
all_variants = list(product([True, False], repeat=5))

print(f"Кількість перевірених комбінацій: {len(all_variants)}\n")

# Заголовок таблиці істинності
print("Emp   Ver   Prem  Adm   Ban   | Base  Prem  Adm   Secr")
print("-" * 57)

# Змінні для аналізу результатів
full_access_count = 0
premium_without_base = []

# Перевіряємо всі комбінації
for emp, ver, prem, adm, ban in all_variants:
    access = check_access(emp, ver, prem, adm, ban)

    # Підрахунок випадків повного доступу
    if all(access.values()):
        full_access_count += 1

    # Пошук Premium-доступу без Base-доступу
    if access["Premium"] and not access["Base"]:
        premium_without_base.append(
            (emp, ver, prem, adm, ban)
        )

    # Виведення рядка таблиці істинності
    print(
        f"{int(emp):<6}"
        f"{int(ver):<6}"
        f"{int(prem):<6}"
        f"{int(adm):<6}"
        f"{int(ban):<6}"
        f"| "
        f"{int(access['Base']):<6}"
        f"{int(access['Premium']):<6}"
        f"{int(access['Admin']):<6}"
        f"{int(access['Secret']):<6}"
    )


# Аналіз результатів
print("\nРезультати аналізу")
print("-" * 57)

print(
    f"Кількість комбінацій із повним доступом: "
    f"{full_access_count}"
)

print("\nКомбінації з доступом Premium, але без доступу Base:")

for emp, ver, prem, adm, ban in premium_without_base:
    print(
        f"Employee={int(emp)}, "
        f"Verified={int(ver)}, "
        f"Premium={int(prem)}, "
        f"Admin={int(adm)}, "
        f"Banned={int(ban)}"
    )

print(
    f"Кількість комбінацій Premium без Base: "
    f"{len(premium_without_base)}"
)

print(
    "\nПояснення: доступ Premium може бути наданий користувачу, "
    "який не є співробітником, але має Premium-підписку, "
    "пройшов верифікацію та не заблокований. Доступ Base "
    "не надається, оскільки для нього обов'язково потрібно "
    "бути співробітником."
)