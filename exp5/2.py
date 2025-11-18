"""
2、实验题目：中文数字对照表
输入一个数字，转换成中文数字。比如：1234567890 -> 壹贰叁肆伍陆柒捌玖零。
"""


def convert_to_chinese(n):
    dict = {
        0: "零",
        1: "壹",
        2: "贰",
        3: "叁",
        4: "肆",
        5: "伍",
        6: "陆",
        7: "柒",
        8: "捌",
        9: "玖",
    }
    res = ""
    for i in str(n):
        res += dict[int(i)]
    return res


print("======中文数字转换器======")
while True:
    n = int(input("请输入一个数字："))
    print(convert_to_chinese(n))
