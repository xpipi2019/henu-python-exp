"""
10.写一个计算可以计算一个人BMI（身体质量指数）指数程序体质指数（BMI）=体重（kg）÷身高^2（m）
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：27-32
非常肥胖, 高于32
"""
def bmi(weight,height):
    return weight / height**2

weight = float(input("请输入体重(kg)："))
height = float(input("请输入身高(cm)："))
height = height / 100
result = bmi(weight,height)
print(f"BMI：{result}")
if result < 18.5:
    print("过轻")
elif result < 23.9:
    print("正常")
elif result < 27:
    print("过重")
elif result < 32:
    print("肥胖")
else:
    print("非常肥胖")
