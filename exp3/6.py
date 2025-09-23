"""
6、编写装饰器，在每次执行目标函数之前先让用户输入用户名和密码，给用户三次机会，登录成功才能访问目标函数。
"""

usr = "admin"
pwd = "123456"


def login(fn):
    def wrapper(*args, **kwargs):
        chances = 3
        while chances:
            inputUsr = input("用户名：")
            inputPwd = input("密码：")
            if inputUsr == usr and inputPwd == pwd:
                print(f"欢迎{usr}")
                return fn(*args, **kwargs)
            else:
                chances = chances - 1
                if chances > 0:
                    print(f"登录错误你还有{chances}次机会")
                else:
                    print("登录超限，请明天再登录。")
                    return

    return wrapper


@login
def func1():
    print("func1")


func1()
