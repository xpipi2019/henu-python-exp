"""
3、下图为动物信息表，数据暂存于CSV文件（animal.csv），动物信息格式为：name表示名称，weigth 表示体重，speed表示动物的奔跑速度(单位:km/h)。请根据下述要求完成题目。

1）请按照动物的速度从高到低进行排序，并输出这组动物的最高速度，最低速度和平均速度，平均速度保留两位小数。
2）统计计算出所有动物中大于平均速度的数量。
3）可视化展示数据，让用户能够直观的看出动物奔跑速度间的差异。
"""

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
data = pd.read_csv("animal.csv")

# 1）按速度从高到低排序
data = data.sort_values(by="speed", ascending=False)
print("1）按速度排序（从高到低）：")
print(data)
print(f"\n   最高速度：{data['speed'].max()} km/h")
print(f"   最低速度：{data['speed'].min()} km/h")
print(f"   平均速度：{data['speed'].mean():.2f} km/h")

# 2）统计大于平均速度的数量
avg_speed = data["speed"].mean()
above_avg = data[data["speed"] > avg_speed]
print(f"\n2）大于平均速度的动物：{len(above_avg)}只")
print(above_avg[["name", "speed"]])

# 3）可视化展示速度差异
plt.figure(figsize=(10, 6))
colors = ["gold" if s > avg_speed else "steelblue" for s in data["speed"]]
bars = plt.bar(data["name"], data["speed"], color=colors)
plt.axhline(
    y=float(avg_speed), color="red", linestyle="--", label=f"平均速度 {avg_speed:.2f}"
)
plt.xlabel("动物名称")
plt.ylabel("速度 (km/h)")
plt.title("动物奔跑速度对比")
plt.legend()

# 显示速度值
for bar, speed in zip(bars, data["speed"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{speed}",
        ha="center",
        va="bottom",
    )

plt.tight_layout()
plt.show()
