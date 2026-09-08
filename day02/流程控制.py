"""if/elif/else 分支和 for 循环练习。"""


def classify_score(score):
    """根据分数给出等级。"""
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def main():
    # if/elif/else 分支练习
    score = 85
    print(f"分数 {score} 的等级：{classify_score(score)}")

    # for 循环练习：遍历列表求总和与平均值
    scores = [78, 92, 65, 88, 70]
    total = 0
    for s in scores:
        total += s
    average = total / len(scores)
    print(f"平均分：{average:.1f}")

    # for 循环 + 分支：找出不及格和优秀的学生
    print("逐个判断等级：")
    for s in scores:
        print(f"  {s} 分 -> {classify_score(s)}")

    # for 循环配合 range 遍历下标
    print("打印下标和分数：")
    for i in range(len(scores)):
        print(f"  scores[{i}] = {scores[i]}")


if __name__ == "__main__":
    main()
