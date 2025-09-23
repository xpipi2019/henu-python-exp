"""
(7)编写函数，参数为一个字符串，返回这个字符串所有子串里面构成回文串的最大子串。
(8)编写函数，输入不定长参数，将其中是整型的全部相加，忽略非整型的参数。（提示：判断是否是整型可以使用isinstance函数）
(9)编写函数，传入函数中多个实参（均为可迭代对象，如字符串、元组、列表、集合等），将每个实参的每个元素依次加入到函数的动态参数args里面，例如传入两个参数[1, 2, 3] (10, 20）最终args为（1,2,3,10,20)
(10)编写函数，传入函数中多个实参（均为字典），将每个实参的每个元素依次加入到函数的动态参数kwargs里面，例如传入两个参数{'one':1} {'two':2}, 最终kwargs为{'one': 1, 'two': 2}。
"""


def task07(s: str):
    max_len = 0
    longest = ""
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                if len(substr) > max_len:
                    max_len = len(substr)
                    longest = substr
    return longest


def task08(*args):
    tot = 0
    for arg in args:
        if isinstance(arg, int):
            tot += arg
    return tot


def task09(*args):
    res = []
    for arg in args:
        for element in arg:
            res.append(element)
    return res


def task10(*args):
    kwargs = {}
    for arg in args:
        for key, value in arg.items():
            kwargs[key] = value
    return kwargs


print(task07("abacabad"))
print(task08(1, 2, 3, 4, 5))
print(task09([1, 2, 3], (10, 20)))
print(task10({"one": 1}, {"two": 2}))
