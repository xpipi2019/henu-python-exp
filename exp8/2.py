"""
利用Matplotlib库，绘制出抛物线曲线图，线为红色圆型点线图，横坐标取值范围：[-10, 10]，绘制点数50，加上坐标轴说明（x轴：x tick，y轴：voltage），图标题为抛物线示意图。
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(-10, 10, 50)
y = x**2
plt.plot(x, y, "r-o")
plt.xlabel("x tick")
plt.ylabel("voltage")
plt.title("抛物线示意图")
plt.show()
