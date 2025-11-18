"""
4、实验题目：商品筛选
有如下商品价格：568，239，368，425，121，219，834，1263，26，请输入随意一个价格区间进行商品的筛选，并能够对筛选出的商品进行从大到小和从小到大进行排序，并求出这个区间的商品的平均价格。
"""

prices = [568, 239, 368, 425, 121, 219, 834, 1263, 26]
lower_bound = int(input("请输入价格下限："))
upper_bound = int(input("请输入价格上限："))
filtered_prices = [price for price in prices if lower_bound <= price <= upper_bound]
filtered_prices.sort(reverse=True)
print(f"从大到小排序后的商品价格：{filtered_prices}")
filtered_prices.sort()
print(f"从小到大排序后的商品价格：{filtered_prices}")
average_price = sum(filtered_prices) / len(filtered_prices)
print(f"这个区间的商品的平均价格：{average_price:.2f}")
