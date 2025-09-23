"""
请使用map函数实现：
1）编写程序，输入一个自然数字符串，然后输出各位数字之和。
2）编写程序，输入一个包含若干整数的列表，把列表中所有整数转换为字符串，然后输出包含这些字符串的列表。
3）编写程序，输入两个包含若干整数的等长列表，把这两个列表看作两个向量，输出这两个向量的内积。
"""


def func1(s: str):
    tot = 0
    for char in s:
        tot += int(char)
    return tot


def func2(lst: list):
    res = []
    for i in range(len(lst)):
        res.append(str(lst[i]))
    return res


def func3(lst1: list, lst2: list):
    min_len = min(len(lst1), len(lst2))
    tot = 0
    for i in range(min_len):
        tot += lst1[i] * lst2[i]
    return tot


print(func1("1234567890"))
print(func2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(func3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
