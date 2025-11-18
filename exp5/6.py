"""
6、实验题目：编写程序，使用列表生成表达式生成一个包含20个随机整数的列表，然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变。（提示，使用切片）
"""

import random

numbers = [random.randint(1, 100) for _ in range(20)]
print(numbers)
numbers[::2] = sorted(numbers[::2], reverse=True)
print(numbers)
