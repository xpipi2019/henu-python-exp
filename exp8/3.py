import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

print("=" * 50)
print("(1) 读取 CSV 文件数据：")
print("=" * 50)
df = pd.read_csv("classInfo.csv")
print(df)
print()

print("=" * 50)
print("(2) 身高统计分析：")
print("=" * 50)

df_sorted = df.sort_values(by="身高", ascending=False)
print("\n按身高从高到低排序：")
print(df_sorted)

avg_height = df["身高"].mean()
print(f"\n班级平均身高：{avg_height:.2f}")

count_above_170 = (df["身高"] > 170).sum()
print(f"身高在170以上的学生数：{count_above_170}")
print()

print("=" * 50)
print("(3) 绘制柱状图...")
print("=" * 50)

plt.figure(figsize=(10, 6))
bars = plt.bar(
    df["姓名"],
    df["身高"],
    color=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336"],
)

for bar, height in zip(bars, df["身高"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        str(height),
        ha="center",
        va="bottom",
        fontsize=12,
    )

plt.axhline(
    y=float(avg_height),
    color="red",
    linestyle="--",
    label=f"平均身高: {avg_height:.2f}",
)

plt.xlabel("学生姓名", fontsize=12)
plt.ylabel("身高 (cm)", fontsize=12)
plt.title("班级学生身高分布情况", fontsize=14)
plt.ylim(150, 185)
plt.legend()
plt.tight_layout()
plt.show()
