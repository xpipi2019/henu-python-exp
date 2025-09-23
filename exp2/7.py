"""
7.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""
import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = math.isqrt(n)
    return sqrt*sqrt == n

print("在范围[-99999, 99999)内，满足条件的x为：")
for x in range(-99999, 99999):
    if is_perfect_square(x + 100) and is_perfect_square(x + 268):
        print(f"{x}",end=" ")