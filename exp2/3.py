"""
3、个人用户登录：
当用户登录时给3次机会。如果成功，显示欢迎xxx。如果登录失败，显示录入错误你还有x次机会。如果3次机会使用完毕，则显示登录超限，请明天再登录。
"""
usr = "admin"
pwd = "123456"

chances = 3
while chances:
    inputUsr = input("用户名：")
    inputPwd = input("密码：")
    if inputUsr == usr and inputPwd == pwd:
        print(f"欢迎{usr}")
        break
    else:
        chances = chances - 1
        if chances > 0:
            print(f"录入错误你还有{chances}次机会")
        else:
            print("登录超限，请明天再登录。")