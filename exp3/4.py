# 4、使用闭包编写一个学生成绩平均统计。要求每次调用函数传入一个学生成绩，得到已经传入成绩的平均分。
def average_score():
    scores = []

    def add_score(score):
        scores.append(score)
        return sum(scores) / len(scores)

    return add_score


avg_score = average_score()
print(avg_score(85))
print(avg_score(90))
print(avg_score(95))
print(avg_score(100))
print(avg_score(80))
print(avg_score(75))
