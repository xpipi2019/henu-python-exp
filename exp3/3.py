# 3、使用高阶函数方式设计Calc函数，实现加、减、乘、除、乘方等计算功能
def Calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "**":
        return a**b


print(Calc(2, 4, "+"))
print(Calc(2, 4, "-"))
print(Calc(2, 4, "*"))
print(Calc(2, 4, "/"))
print(Calc(2, 4, "**"))
