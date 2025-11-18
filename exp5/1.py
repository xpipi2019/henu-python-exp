"""
1、实验题目：好友管理系统
请设计一个好友管理系统，每个功能都对应一个序号，用户可根据提示“请输入您的选项”选择序号执行相应的操作，包括：
（1）添加好友：用户根据提示“请输入要添加的好友：”输入要添加好友的姓名，添加后会提示“好友添加成功”。
（2）删除好友：用户根据提示“请输入删除好友姓名：”输入要删除好友的姓名，删除后提示“删除成功”。
（3）备注好友：用户根据提示“请输入要修改的好友姓名：”和“请输入修改后的好友姓名：”分别输入修改前和修改后的好友姓名，修改后会提示“备注成功”。
（4）展示好友：若用户还没有添加过好友，提示“好友列表为空”，否则返回每个好友的姓名。
（5）退出：关闭好友系统。
"""


class FriendManager:
    def __init__(self):
        self.friends = []

    def add_friend(self, name):
        self.friends.append(name)
        print(f"好友 {name} 添加成功")

    def delete_friend(self, name):
        self.friends.remove(name)
        print(f"好友 {name} 删除成功")

    def modify_friend(self, name, new_name):
        self.friends[self.friends.index(name)] = new_name
        print(f"好友 {name} 备注成功")

    def show_friends(self):
        if len(self.friends) == 0:
            print("好友列表为空")
        else:
            print("好友列表：")
            for friend in self.friends:
                print(friend, end=" ")
            print()

    def exit(self):
        print("关闭好友系统")
        exit()

    def run(self):
        print("======好友管理系统======")
        while True:
            print("1.添加好友")
            print("2.删除好友")
            print("3.备注好友")
            print("4.展示好友")
            print("5.退出")
            choice = int(input("请输入您的选项(1-5)："))
            if choice == 1:
                self.add_friend(input("请输入要添加的好友："))
            elif choice == 2:
                self.show_friends()
                self.delete_friend(input("请输入删除好友姓名："))
            elif choice == 3:
                self.show_friends()
                self.modify_friend(
                    input("请输入要修改的好友姓名："), input("请输入修改后的好友姓名：")
                )
            elif choice == 4:
                self.show_friends()
            elif choice == 5:
                self.exit()
            else:
                print("输入错误")


friend_manager = FriendManager()
friend_manager.run()
