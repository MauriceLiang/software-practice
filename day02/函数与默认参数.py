"""函数定义与使用默认参数的练习。"""


def greet(name, greeting="你好"):
    """greeting 是默认参数，调用时不传就使用默认值。"""
    return f"{greeting}，{name}"


def add(num1, num2=0, num3=0):
    """默认参数让调用方可以按需传入 2 个或 3 个数。"""
    return num1 + num2 + num3


def make_profile(name, age, major="软件工程", hobby="阅读"):
    """多个默认参数组合，返回一个描述字符串。"""
    return f"姓名：{name}，年龄：{age}，专业：{major}，爱好：{hobby}"


def main():
    # 使用默认参数，不传 greeting
    print(greet("张三"))
    # 覆盖默认参数
    print(greet("李四", "早上好"))

    # 默认参数的不同调用方式
    print(add(1, 2))          # num3 用默认值 0
    print(add(1, 2, 3))       # 三个数都传

    print(make_profile("王五", 20))
    print(make_profile("赵六", 22, "计算机", "篮球"))


if __name__ == "__main__":
    main()
