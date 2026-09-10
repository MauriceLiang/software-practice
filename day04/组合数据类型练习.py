"""组合数据类型练一练：元组拆包、集合去重、列表套字典。"""

# 练习3（嵌套）用的学生花名册：列表里放字典
STUDENTS = [
    {"name": "小明", "score": 92},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 76},
]


def practice1():
    """练习1（元组）：坐标拆包。"""
    point = (116, 39)
    x, y = point  # 拆包：把元组里的两个值分别赋给 x、y
    print(f"x = {x}, y = {y}")


def practice2():
    """练习2（集合）：用 set 去重，打印去重后的人数。"""
    names = ["小明", "小红", "小明", "小刚", "小红", "小明"]
    unique_names = set(names)  # set 自动去掉重复元素
    print(f"去重前 {len(names)} 人，去重后 {len(unique_names)} 人")


def practice3():
    """练习3（嵌套）：遍历学生花名册，打印每个人的名字和成绩。"""
    for student in STUDENTS:
        print(f'{student["name"]}：{student["score"]} 分')


def challenge():
    """挑战：比较 score，找出分数最高的同学并打印名字。"""
    top = STUDENTS[0]  # 先假设第一个是最高分
    for student in STUDENTS:
        if student["score"] > top["score"]:
            top = student  # 遇到更高的就换人
    print(f'最高分是 {top["name"]}，{top["score"]} 分')


def main():
    practice1()
    practice2()
    practice3()
    challenge()


if __name__ == "__main__":
    main()
