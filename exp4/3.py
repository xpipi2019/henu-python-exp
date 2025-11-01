"""
3、 实验题目：类的创建
教材P115， 第34题
定义Circle类，要求：包括私有属性_radius，构造函数为半径赋值，构造函数的默认参数值为0，析构函数输出适当信息，普通方法SetRadius用于设置半径，普通方法Area返回圆面积，内置方法_str_用于输出圆面积，内置方法_gt_用于比较两个圆面积大小，并创建两个实例分别验证上述功能。
"""

import math


class Circle:
    def __init__(self, radius=0):
        self.__radius = radius
        print(f"已创建半径为{self.__radius}的圆")

    def SetRadius(self, radius):
        self.__radius = radius
        print(f"已设置半径为{self.__radius}的圆")

    def Area(self):
        return math.pi * self.__radius**2

    def __str__(self):
        return f"圆的面积为{self.Area():.2f}"

    def __gt__(self, other):
        return self.Area() > other.Area()


circle1 = Circle(10)
circle2 = Circle(20)
circle3 = Circle()
print(circle1.Area())
print(circle2.Area())
print(circle3.Area())

circle3.SetRadius(30)
print(circle1.__str__())
print(circle2.__str__())
print(circle3.__str__())

if circle1.__gt__(circle2):
    print("circle1的面积大于circle2的面积")
else:
    print("circle1的面积小于circle2的面积")

if circle3.__gt__(circle2):
    print("circle3的面积大于circle2的面积")
else:
    print("circle3的面积小于circle2的面积")
