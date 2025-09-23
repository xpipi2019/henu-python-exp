"""
8.一个雇员一周的总薪水，等于其每小时的时薪，乘以其一周工作的正常小时数，再加上加班费。加班费等于总的加班时间，乘以每小时薪水的1.5倍。
编写一个程序，以每小时的薪水，常规工作时间，加班工作时间作为输入，显示一个雇员的总周薪。按照要求：每周常规工作时间不能超过40小时且不能小于等于0,正常工作时薪不能小于15元。
"""
salaryperhour = float(input("每小时的薪水："))
normalhours = float(input("常规工作时间："))
overtimehours = float(input("加班工作时间："))

if salaryperhour < 15 or normalhours <= 0 or normalhours > 40 or overtimehours < 0:
    print("输入不符合要求")
else:
    result = salaryperhour * normalhours + salaryperhour * 1.5 * overtimehours
    print(f"总周薪：{result}")
