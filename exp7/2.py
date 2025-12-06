"""
2、实验题目：文件读取
将StudentInfo中的信息以字典的形式存储在列表里。
[{'学号': '1445204009', '姓名': '王召', '平时成绩': '100', '期末成绩': '90'},
 {'学号': '1445204013', '姓名': '林锦', '平时成绩': '95', '期末成绩': '67'}
 ...
]
"""

with open("StudentInfo.csv", "r") as file:
    data = file.readlines()
    students = []
    for line in data:
        line = line.strip()
        if line == "":
            continue
        data = line.split(",")
        students.append(
            {"学号": data[0], "姓名": data[1], "平时成绩": data[2], "期末成绩": data[3]}
        )
    print(students)
