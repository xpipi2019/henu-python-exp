"""
8、实验题目：统计词频  （选做）
给一段文本，例如：“who have an apple apple is free free is money you know”，请统计单词出现的次数。（提示：需要用正则表达式去掉标点符号和空格）
"""

import re

text = "who have an apple apple is free free is money you know"
words = re.findall(r"\b\w+\b", text)
print(text)
# print(words)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
