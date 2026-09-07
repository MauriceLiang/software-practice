"""升级版个人名片，练习 f-string 对齐和运算符计算。"""


def main():
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    major = input("请输入专业：")
    hobby = input("请输入爱好：")

    border = "=" * 40
    print(border)
    print(f"{'个人名片':^40}")
    print(border)
    print(f"{'姓名':<8}：{name}")
    print(f"{'年龄':<8}：{age} 岁")
    print(f"{'专业':<8}：{major}")
    print(f"{'爱好':<8}：{hobby}")
    print(f"{'明年年龄':<6}：{age + 1} 岁")
    print(border)


if __name__ == "__main__":
    main()
