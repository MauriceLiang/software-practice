"""输入、输出和基本整数运算练习。"""


def main():
    name = input("请输入你的姓名：\n")
    age = input("请输入你的年龄：\n")
    print(f"大家好，我叫{name}，我今年{age}岁了。")

    num1 = 9
    num2 = 3
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")


if __name__ == "__main__":
    main()
