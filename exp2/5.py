"""
5.银行金额大写汉字转换：
银行电子支票业务在金额部分需要使用大写的汉字，因此需要将用户录入的数字信息转变为汉字。目前只需完成1~5位整数转换即可。
"""
def solve(n):
    if n < 1 or n > 99999:
        return "超出转换范围！"
    if n == 0:
        return "零"
    
    digit_map = "零壹贰叁肆伍陆柒捌玖"
    unit_map = ["", "拾", "佰", "仟", "万"]
    
    num_str = str(n)
    length = len(num_str)
    result = ""
    
    for i, digit_char in enumerate(num_str):
        digit = int(digit_char)
        pos = length - i - 1  # 当前位置
        
        if digit != 0:
            # 非零数字：添加数字 + 单位
            result += digit_map[digit] + unit_map[pos]
        else:
            # 零数字
            if i < length - 1:
                has_non_zero_after = any(int(d) != 0 for d in num_str[i+1:])
                if has_non_zero_after and not result.endswith("零"):
                    result += "零"
    
    return result

while True:
    user_input = input("请输入存入金额（输入0退出）：")
    if user_input == "0":
        break
    result = solve(int(user_input))
    print(f"数字 {user_input} 的汉字大写为：{result}")
    