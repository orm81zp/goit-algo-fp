import sys


def parse_arguments():
    """Парсить аргументи командного рядка"""

    budget = 75

    if len(sys.argv) > 1:
        try:
            budget = int(sys.argv[1])
        except Exception:
            print("Бюджет має бути числом, наприклад: 75")

    return budget


def greedy_algorithm(items, budget):
    # сортування
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, values in sorted_items:
        if total_cost + values["cost"] <= budget:
            chosen_items.append(item)
            total_cost += values["cost"]
            total_calories += values["calories"]

    return chosen_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    chosen_items = set()

    for i, (_, values) in enumerate(items.items(), start=1):
        for j in range(budget + 1):
            if values["cost"] <= j:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - values["cost"]] + values["calories"]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    total_calories = dp[n][budget]

    i = n
    j = budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.add(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    total_cost = sum(items[item]["cost"] for item in chosen_items)
    return list(chosen_items), total_cost, total_calories


def print_results(name, result):
    items, total_cost, total_calories = result
    print(f"{name}:")
    print(f"Обрані елементи їжі: {items}")
    print(f"Загальна вартість: {total_cost}")
    print(f"Загальна кількість калорій: {total_calories}")
    print()


def main():
    budget = parse_arguments()
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    print(f"Обмеження бюджету: {budget}")
    print_results("Жадібний алгоритм", greedy_algorithm(items, budget))
    print_results(
        "Динамічний алгоритм",
        dynamic_programming(items, budget),
    )


if __name__ == "__main__":
    main()
