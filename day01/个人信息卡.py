"""个人信息卡。"""


def main():
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    major = input("请输入专业：")
    hobby = input("请输入爱好：")

    print("\n个人信息卡")
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"专业：{major}")
    print(f"爱好：{hobby}")


if __name__ == "__main__":
    main()
