"""
3、实验题目：学生成绩管理

将学生对象存入列表中，并按成绩对学生进行排序,并获取成绩最高和成绩最低的学生信息，并将最高分和最低分的学生从列表删除，最后再对列表进行拷贝，对拷贝的列表进行翻转输出。
"""


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"姓名: {self.name}, 成绩: {self.score}"

    def show_students(self):
        for student in students:
            print(student)


students = []
student1 = Student("张三", 85)
student2 = Student("李四", 90)
student3 = Student("王五", 75)
student4 = Student("赵六", 80)
student5 = Student("孙七", 70)
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)
print("原始学生列表：")
students[0].show_students()
students.sort(key=lambda x: -x.score)
print("排序后的学生列表：")
students[0].show_students()
print("最高分学生：")
print(students[0])
print("最低分学生：")
print(students[-1])
students.remove(students[0])
students.remove(students[-1])
print("删除最高分和最低分后的学生列表：")
students[0].show_students()
copied_students = students.copy()
copied_students.reverse()
print("拷贝的列表翻转后：")
for student in copied_students:
    print(student)
