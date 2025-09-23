"""
9.水仙花数是3位整数（100-199），它的各位数字立方和等于该数本身。请编写程序。
"""
def is_narcissistic(n):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    return a**3 + b**3 + c**3 == n

for i in range(100,200):
    if is_narcissistic(i):
        print(i,end=" ")