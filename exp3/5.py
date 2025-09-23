"""
5、给每个函数写一个记录日志的功能，要求，每次一调用函数之前，都要将函数名称，时间节点记输出。
请使用strftime()获取年月日时分秒。函数名：fn.__name__
"""

import time


def log(fn):
    def wrapper(*args, **kwargs):
        print(f"函数名称：{fn.__name__}，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
        return fn(*args, **kwargs)

    return wrapper


@log
def func1():
    print("func1")
    time.sleep(1)


@log
def func2():
    print("func2")
    time.sleep(2)


func1()
func2()
func1()
