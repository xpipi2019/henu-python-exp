"""
2、实验题目：添加实例方法
1）定义学生类Student，构造方法的两个参数name和year，将它们保存为实例变量。创建一个对象：Jerry，5年级。
2）定义成绩类Grade，并定义及格线属性：passing为60。添加构造方法，通过参数传值给实例变量score。
3）Student类的构造方法中，声明一个空的成绩列表grades。在Student中添加一个方法add_grade(Grade)，该方法需要首先验证传入的参数类型是否为Grade，正确的话可以添加到成绩列表中，否则不执行添加操作。
4）创建5个Grade对象，成绩分别为100,90,85,88,70分，并将它们放入Jerry的成绩列表里。
5）Grade中添加is_passing方法，返回该成绩是否及格。
6）Student中添加一个返回该生的平均成绩的方法get_average().
7）判断Jerry是否有不及格成绩。
8）输出Jerry的平均成绩。
"""


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)

    def get_average(self):
        return sum(grade.score for grade in self.grades) / len(self.grades)

    def has_failing(self):
        return any(grade.is_passing() for grade in self.grades)

    def __str__(self):
        return f"Student: {self.name}, Year: {self.year}"


jerry = Student("Jerry", 5)


class Grade:
    passing = 60

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return self.score >= Grade.passing


grades = [Grade(100), Grade(90), Grade(80), Grade(70), Grade(50)]
for grade in grades:
    jerry.add_grade(grade)

print(f"Jerry是否有不及格成绩: {'是' if jerry.has_failing() else '否'}")
print(f"Jerry的平均成绩: {jerry.get_average():.2f}")
