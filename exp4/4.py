"""
4、实验题目：类别统计
设计一个函数def func(*args)，用来统计当前文件中方法、函数、Animal类对象的个数。（用中文和阿拉伯数字输出最后的结果）
"""

import inspect
import sys


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} is speaking"


def func(*args):
    current_module = sys.modules[__name__]

    method_count = 0
    function_count = 0
    animal_object_count = 0

    for name, obj in inspect.getmembers(current_module):
        if name.startswith("_") or inspect.ismodule(obj):
            continue

        if inspect.isfunction(obj):
            function_count += 1

        elif isinstance(obj, Animal):
            animal_object_count += 1

        elif inspect.isclass(obj):
            for method_name, method_obj in inspect.getmembers(
                obj, predicate=inspect.isfunction
            ):
                method_count += 1

    print(f"方法数量：{method_count}")
    print(f"函数数量：{function_count}")
    print(f"Animal类对象数量：{animal_object_count}")

    return method_count, function_count, animal_object_count


def test_func():
    return "testtest"


def test_func2(x, y):
    return x + y


def test_func3(x, y):
    return True


dog = Animal("Dog")
cat = Animal("Cat")
func()
