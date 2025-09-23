"""
1.实验题目：学生宿舍信息输入
模拟学生宿舍信息输入，需要输入学生个人信息：姓名、性别、年龄、宿舍号、学院、专业、电话信息，并输出显示。
"""
print("请输入你的个人信息：")
name = input("姓名：")
sex = input("性别：")
age = input("年龄：")
dornum = input("宿舍号：")
academy = input("学院：")
major = input("专业：")
phone = input("电话：")
print(f'''你的个人信息如下：
姓名：{name}
性别：{sex}
年龄：{age}
宿舍号：{dornum}
学院：{academy}
专业：{major}
电话：{phone}''')