
"""
4.模拟斐波那契数列输出：
用户输入指定的数列范围，正确输出结果。
"""
def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a)
        a,b = b,a+b

n = input("请输入指定的数列范围(1~n)：")
n = int(n)
fib(n)