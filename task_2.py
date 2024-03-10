import matplotlib.pyplot as plt
import sys
import numpy as np


def parse_arguments():
    """Парсить аргументи командного рядка"""

    depth_of_recursion = 10

    if len(sys.argv) > 1:
        try:
            depth_of_recursion = int(sys.argv[1])
        except Exception:
            print("рівень рекурсії має бути числом, наприклад: 10")

    return depth_of_recursion


def draw_tree(depth, ax, x, y, size, angle):
    if depth == 0:
        return

    x1 = x + size * np.cos(np.deg2rad(angle))
    y1 = y + size * np.sin(np.deg2rad(angle))

    size = size * np.sqrt(2) / 2

    x_values = [x, x1]
    y_values = [y, y1]

    ax.plot(x_values, y_values, color="red")

    draw_tree(depth - 1, ax, x1, y1, size, angle - 45)
    draw_tree(depth - 1, ax, x1, y1, size, angle + 45)


def main():
    depth_of_recursion = parse_arguments()
    _, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    draw_tree(depth_of_recursion, ax, 0, 0, 1, 90)
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
