# (11)解一元二次方程。func（a, b, c）求x1， x2
import math


def func(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return "无解"
    elif delta == 0:
        return "x = " + str(-b / (2 * a))
    else:
        return (
            "x1 = "
            + str((-b + math.sqrt(delta)) / (2 * a))
            + " x2 = "
            + str((-b - math.sqrt(delta)) / (2 * a))
        )


print(func(1, -5, 6))
print(func(1, -4, 4))
print(func(1, 0, -4))
print(func(1, 2, 5))
