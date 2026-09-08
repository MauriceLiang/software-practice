"""字典的取值、添加与遍历练习。"""


def main():
    # 创建字典
    student = {"name": "张三", "score": 85, "major": "软件工程"}

    # 取值
    print(f"姓名：{student['name']}")
    print(f"分数：{student['score']}")
    # 用 get 取值，键不存在时返回默认值，不会报错
    print(f"年龄：{student.get('age', '未知')}")

    # 添加/修改
    student["age"] = 20
    print(f"添加年龄后：{student}")
    student["score"] = 90
    print(f"修改分数后：{student}")

    # 遍历：遍历键值对
    print("遍历所有键值对：")
    for key, value in student.items():
        print(f"  {key} = {value}")

    # 遍历键 / 遍历值
    print(f"所有键：{list(student.keys())}")
    print(f"所有值：{list(student.values())}")

    # 统计某个字符串中每个字符出现的次数（字典常见用途）
    text = "hello python"
    counter = {}
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
    print(f"字符出现次数：{counter}")


if __name__ == "__main__":
    main()
