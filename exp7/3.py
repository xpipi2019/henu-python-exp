"""
3、实验题目：字典格式读取文件
现有一个user.csv文件，内容如下：
name,username,email
杨洋,yangy,yangy@sina.com
贾子豪,jiazh,jiazh@126.com
于飞,yuf,yuf@163.com
田宇辰,tianych,tianych@sina.com
1)以字典格式读取csv文件并打印出每个人的名字和电子邮件地址
2)新建usercopy.csv文件，将user.csv文件的内容按照csv文件写入的方式写入进usercopy.csv中。
"""

with open("user.csv", "r") as file:
    data = file.readlines()
    users = []
    for line in data:
        line = line.strip()
        if line == "":
            continue
        data = line.split(",")
        users.append({"name": data[0], "username": data[1], "email": data[2]})
    print(users)

with open("usercopy.csv", "w") as file:
    for user in users:
        file.write(f"{user['name']},{user['username']},{user['email']}\n")
