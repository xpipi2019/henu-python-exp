"""
5、实验题目：生成验证码
验证码一般是包括一些随机产生的数字或符号，请实现随机生成一组6位验证码的功能。
每个字符可以是大写字母、小写字母或数字，有且只能是这三种类型中的一种。
"""

import random


def generate_verification_code():
    code = ""
    for _ in range(6):
        code += random.choice(
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
    return code


print(generate_verification_code())
