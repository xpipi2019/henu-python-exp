"""
3、获取字符串中的第一个唯一字符。
要求：给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
示例：
输入: "leetcode"
输出: 0
"""


def get_first_unique_char(s: str):
    for char in s:
        if s.count(char) == 1:
            return s.index(char)
    return -1


print(get_first_unique_char("leetcode"))
print(get_first_unique_char("loveleetcode"))
print(get_first_unique_char("aabb"))
