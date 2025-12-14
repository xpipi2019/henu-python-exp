"""
1.使用Pandas 打开'StudentInfo.xlsx'文件，
1）查看data的统计信息
2）处理空值，将平时成绩和期末成绩中的缺失值填空为0
3）处理重复值，去除学号这列的重复数据,保留重复行中的最后一行
4）处理异常值， 检查期末成绩有没有异常值（<0 或者>100)
5）统计计算出期末成绩的平均计分、最大、最小、以及90分以上的人员个数和具体人员信息
6）按照'60分以下','60-70分','70-80分','80-90分','90-100分'统计成绩分布，并绘图显示。
"""

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
data = pd.read_csv("StudentInfo.csv")

# 1）统计信息
print("1）统计信息：")
print(data.describe())

# 2）处理空值
data["平时成绩"] = data["平时成绩"].fillna(0)
data["期末成绩"] = data["期末成绩"].fillna(0)
print("\n2）空值已填充为0")

# 3）处理重复值
print(f"\n3）去重前：{len(data)}行")
data = data.drop_duplicates(subset=["学号"], keep="last")
print(f"   去重后：{len(data)}行")

# 4）检查异常值
abnormal = data[(data["期末成绩"] < 0) | (data["期末成绩"] > 100)]
print(f"\n4）异常值（<0或>100）：{len(abnormal)}条")
if len(abnormal) > 0:
    print(abnormal[["学号", "姓名", "期末成绩"]])

# 5）期末成绩统计
valid_data = data[(data["期末成绩"] >= 0) & (data["期末成绩"] <= 100)]
above_90 = valid_data[valid_data["期末成绩"] >= 90]
print(
    f"\n5）期末成绩：平均{valid_data['期末成绩'].mean():.2f} | "
    f"最高{valid_data['期末成绩'].max()} | 最低{valid_data['期末成绩'].min()}"
)
print(f"   90分以上：{len(above_90)}人")
print(above_90[["学号", "姓名", "期末成绩"]])

# 6）成绩分布统计及绘图
bins = [0, 60, 70, 80, 90, 101]
labels = ["60分以下", "60-70分", "70-80分", "80-90分", "90-100分"]
grade_cut = pd.cut(valid_data["期末成绩"], bins=bins, labels=labels, right=False)
grade_counts = pd.Series(grade_cut).value_counts().sort_index()
print(f"\n6）成绩分布：\n{grade_counts}")

# 绘图
plt.figure(figsize=(10, 6))
x_labels = [str(x) for x in grade_counts.index]
y_values = list(grade_counts.values)
bars = plt.bar(
    x_labels, y_values, color=["red", "orange", "yellow", "lightgreen", "green"]
)
plt.xlabel("成绩等级")
plt.ylabel("人数")
plt.title("期末成绩分布统计图")
for bar, count in zip(bars, y_values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        str(count),
        ha="center",
        va="bottom",
    )
plt.tight_layout()
plt.show()
