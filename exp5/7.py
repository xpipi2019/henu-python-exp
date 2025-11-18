"""
7、实验题目：编写程序，使用列表生成表达式生成一个包含50个随机整数的列表，然后删除其中所有奇数（提示：从后向前删。）
"""

import random

numbers = [random.randint(1, 100) for _ in range(50)]
print(numbers)
numbers = [num for num in numbers if num % 2 == 0]
print(numbers)
