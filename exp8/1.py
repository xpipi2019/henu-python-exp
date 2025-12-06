import numpy as np

ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("原始数组：")
print(ndarray)
print()

print("切片1：")
print(ndarray[1:, :2])

print("切片2：")
print(ndarray[::, 1:2])

print("切片3：")
print(ndarray[1:2, 2:3])

print("切片4：")
print(ndarray[1:2, ::])

"""
将数组中的每个元素乘2后，按行和按列方式分别计算其最大值，打印输出结果
"""
print("按行方式计算最大值：")
print(np.max(ndarray * 2, axis=1))
print("按列方式计算最大值：")
print(np.max(ndarray * 2, axis=0))
