"""
2、下图为某公司某部门员工的业绩计分表，数据存储于staff.csv中，该部门负责人需要了解所有人员的平均业绩情况。请按下述要求完成数据处理。

1）将文件staff.csv中的数据读入，并根据所学知识，选用一种合适的存储结构存储到内存中。
2）选用合适的一种方法，清除表中的不完整数据（含有空值的数据记录均要清除）。
3）统计计算出所有有效人员的平均计分及90分以上的人员数。
4）选用一种合适的图表展示所有有效人员的计分值，显示姓名和计分。
"""

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1）读取CSV文件，使用DataFrame存储
data = pd.read_csv("staff.csv")
print("1）原始数据：")
print(data)

# 2）清除含有空值的记录
print(f"\n2）清洗前：{len(data)}条记录")
data = data.dropna()
print(f"   清洗后：{len(data)}条记录")
print(data)

# 3）统计平均分和90分以上人数
avg_score = data["计分"].mean()
above_90 = data[data["计分"] >= 90]
print(f"\n3）平均计分：{avg_score:.2f}")
print(f"   90分以上：{len(above_90)}人")

# 4）绘制柱状图展示计分
plt.figure(figsize=(10, 6))
bars = plt.bar(data["姓名"], data["计分"], color="steelblue")
plt.xlabel("姓名")
plt.ylabel("计分")
plt.title("员工业绩计分表")
plt.ylim(0, 100)

# 在柱状图上显示分数
for bar, score in zip(bars, data["计分"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{int(score)}",
        ha="center",
        va="bottom",
    )

plt.tight_layout()
plt.show()
