"""
1、实验题目：编写一个学生类，要求有一个计数器的属性，每次实例化后统计实例化了多少个学生。
"""


class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
        print(f"总数:{Student.count}")


student1 = Student("张三", 20)
student2 = Student("李四", 21)
student3 = Student("王五", 22)
