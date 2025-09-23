"""
(4)编写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，并返回。
(5)编写函数，返回两个数字参数中较大的那个数字
(6)编写函数，接收多个数字，求和并返回。
"""


def calcAll(s: str):
    digit_count = 0
    letter_count = 0
    space_count = 0
    other_count = 0
    for char in s:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1
    return {
        "数字": digit_count,
        "字母": letter_count,
        "空格": space_count,
        "其他": other_count,
    }


def getMax(a, b):
    return a if a > b else b


def mySum(*args):
    tot = 0
    for arg in args:
        tot += arg
    return tot


print(calcAll("Hello 123 World! @#$"))
print(getMax(getMax(10, 20), 30))
print(mySum(1, 2, 3, 4, 5))
