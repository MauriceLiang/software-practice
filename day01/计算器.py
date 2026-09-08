"""简单的四则运算计算器。"""


def calculate(num1, num2, operator):
    """根据运算符计算结果；除数为 0 时返回错误提示。"""
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            return "除数不能为 0"
        return num1 / num2
    return "不支持的运算符，请输入 +、-、* 或 /"


def main():
    try:
        num1 = float(input("请输入第一个数："))
        num2 = float(input("请输入第二个数："))
        operator = input("请输入运算符（+、-、*、/）：").strip()
    except ValueError:
        print("请输入有效的数字。")
        return

    result = calculate(num1, num2, operator)
    print(f"计算结果：{result}")


if __name__ == "__main__":
    main()
