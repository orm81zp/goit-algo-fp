import random
import sys
import time

random.seed(time.time())


def parse_arguments():
    """Парсить аргументи командного рядка"""

    dice_rolls = 1000
    N = 15000

    if len(sys.argv) > 2:
        try:
            dice_rolls = int(sys.argv[1])
            N = int(sys.argv[2])
        except Exception:
            print(
                "Кількість кидків кубиків та число згенерованих точок мають бути числами, наприклад: 1000 15000"
            )
    elif len(sys.argv) > 1:
        try:
            dice_rolls = int(sys.argv[1])
        except Exception:
            print("Кількість кидків кубиків має бути числом, наприклад: 1000")

    return dice_rolls, N


def monte_carlo(dice_rolls, N):
    average_map_of_sums = {}

    for _ in range(dice_rolls):
        points = [(random.randint(1, 6), random.randint(1, 6)) for _ in range(N)]

        map_of_sums = {}
        # Відбір точок, що дають потрібну суму
        for point in points:
            sum = point[0] + point[1]
            if sum not in map_of_sums.keys():
                map_of_sums[sum] = 0
            map_of_sums[sum] += 1

        for key, value in map_of_sums.items():
            map_of_sums[key] = value / N
            if key not in average_map_of_sums:
                average_map_of_sums[key] = 0
            average_map_of_sums[key] += map_of_sums[key]

    for key, value in average_map_of_sums.items():
        average_map_of_sums[key] /= dice_rolls
    return average_map_of_sums


def main():
    dice_rolls, N = parse_arguments()
    map_of_sums = monte_carlo(dice_rolls, N)

    print("{:<10} | {:<15}".format("Сума", "Імовірність"))
    for i in range(2, 13):
        print("{:<10} | {:<15}".format(i, str(round(map_of_sums[i] * 100, 2)) + "%"))


if __name__ == "__main__":
    main()
