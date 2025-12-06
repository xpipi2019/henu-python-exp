"""
1、实验题目：给定两个文件路径file1.txt和file2.txt，要求编写一个Python脚本，实现以下功能：
读取这两个文件的内容。
将file2.txt的内容追加到file1.txt的内容之后。
将合并后的内容保存为一个新文件merged.txt。
"""

with open("file1.txt", "r") as file1:
    content1 = file1.read()
with open("file2.txt", "r") as file2:
    content2 = file2.read()
with open("merged.txt", "w") as merged_file:
    merged_file.write(content1)
    merged_file.write(content2)
