"""列表的增删改查与基本切片练习。"""


def main():
    # 初始列表
    numbers = [10, 20, 30, 40, 50]
    print(f"初始列表：{numbers}")

    # 增：追加、插入
    numbers.append(60)
    print(f"追加 60 后：{numbers}")
    numbers.insert(0, 5)
    print(f"开头插入 5 后：{numbers}")

    # 删：按值删除、按下标删除、弹出末尾元素
    numbers.remove(20)
    print(f"删除 20 后：{numbers}")
    del numbers[0]
    print(f"删除第一个元素后：{numbers}")
    last = numbers.pop()
    print(f"弹出末尾元素 {last} 后：{numbers}")

    # 改：按下标修改
    numbers[0] = 99
    print(f"把第一个元素改成 99 后：{numbers}")

    # 查：下标取值、判断是否存在
    print(f"第一个元素：{numbers[0]}")
    print(f"30 在列表中吗：{30 in numbers}")

    # 基本切片
    print(f"前两个元素：{numbers[:2]}")
    print(f"后两个元素：{numbers[-2:]}")
    print(f"从下标 1 到 3：{numbers[1:3]}")
    print(f"隔一个取一个：{numbers[::2]}")
    print(f"反转列表：{numbers[::-1]}")


if __name__ == "__main__":
    main()
