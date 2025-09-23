"""
(1)编写函数，检查获取传入列表或者元组对象的所有奇数位索引对应的元素。
(2)编写函数，判断用户传入的对象（字符串、元组、列表）长度是否大于6。
(3)编写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者。
"""


def check01(seq):
    return [seq[i] for i in range(len(seq)) if i % 2 == 1]


def check02(obj):
    return len(obj) > 6


def check03(lst):
    return lst[:2] if len(lst) > 2 else None


print(check01([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(check01((1, 3, 5, 7, 9)))

print(check02("hello"))
print(check02((1, 2, 3, 4, 5, 6, 7, 8, 9)))

print(check03([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(check03([1, 2]))
