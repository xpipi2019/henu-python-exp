"""
9、实验题目：将下列数据用字典元素列表存储，按照成绩从高到低进行排序后，输出所有学生信息，并输出所有学生的平均分（用列表生成式方法）。
name age grade
ss 18 87
ls 19 92
ww 18 93
zl 18 87
"""

students = [
    {"名字": "ss", "年龄": 18, "成绩": 87},
    {"名字": "ls", "年龄": 19, "成绩": 92},
    {"名字": "ww", "年龄": 18, "成绩": 93},
    {"名字": "zl", "年龄": 18, "成绩": 87},
]
students.sort(key=lambda x: -x["成绩"])
print("按照成绩从高到低排序后的学生信息：")
for student in students:
    print(student)
average_grade = sum(student["成绩"] for student in students) / len(students)
print(f"所有学生的平均分：{average_grade:.2f}")
