graph = {
    "Анна": ["Богдан", "Віктор", "Ганна"],
    "Богдан": ["Анна", "Віктор", "Дмитро"],
    "Віктор": ["Анна", "Богдан", "Ганна", "Дмитро"],
    "Ганна": ["Анна", "Віктор", "Євген"],
    "Дмитро": ["Богдан", "Віктор", "Євген"],
    "Євген": ["Ганна", "Дмитро"]
}

employees = list(graph.keys())

print("Список суміжності:")
print("-" * 45)

for employee, contacts in graph.items():
    print(f"{employee}: {', '.join(contacts)}")

adjacency_matrix = []

for employee in employees:
    row = []

    for other_employee in employees:
        if other_employee in graph.get(employee):
            row.append(1)
        else:
            row.append(0)

    adjacency_matrix.append(row)

print("\nМатриця суміжності:")
print("-" * 45)

print("    ", end="")

for number in range(1, len(employees) + 1):
    print(f"{number:<3}", end="")

print()

for number, row in enumerate(adjacency_matrix, start=1):
    print(f"{number:<4}", end="")

    for value in row:
        print(f"{value:<3}", end="")

    print()

print("\nНумерація співробітників:")

for number, employee in enumerate(employees, start=1):
    print(f"{number} - {employee}")

edges = []

for employee, contacts in graph.items():
    for contact in contacts:
        if (contact, employee) not in edges:
            edges.append((employee, contact))

print("\nСписок унікальних ребер:")
print("-" * 45)

for employee, contact in edges:
    print(f"{employee} - {contact}")

print(f"\nКількість ребер: {len(edges)}")

degrees = {}

for employee, contacts in graph.items():
    degrees[employee] = len(contacts)

print("\nСтепені вершин:")
print("-" * 45)

for employee, degree in degrees.items():
    print(f"{employee}: {degree}")

max_degree = max(degrees.values())
min_degree = min(degrees.values())

most_communicative = []

for employee, degree in degrees.items():
    if degree == max_degree:
        most_communicative.append(employee)

least_communicative = []

for employee, degree in degrees.items():
    if degree == min_degree:
        least_communicative.append(employee)

print(
    f"\nНайбільш комунікабельний: "
    f"{', '.join(most_communicative)}, "
    f"кількість зв'язків: {max_degree}"
)

print(
    f"Найменш комунікабельний: "
    f"{', '.join(least_communicative)}, "
    f"кількість зв'язків: {min_degree}"
)

sum_degrees = sum(degrees.values())
double_edges = 2 * len(edges)

print("\nПеревірка теореми про суму степенів:")
print("-" * 45)

print(f"Сума степенів усіх вершин: {sum_degrees}")
print(f"Кількість ребер: {len(edges)}")
print(f"Подвоєна кількість ребер: {double_edges}")

if sum_degrees == double_edges:
    print(
        f"Рівність виконується: "
        f"{sum_degrees} = 2 * {len(edges)} = {double_edges}"
    )
else:
    print("Рівність не виконується")