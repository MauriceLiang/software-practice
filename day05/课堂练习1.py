"""课堂练习①·函数三题：问候函数、带默认参数的计算器、*args 求和。"""


def hello(name):
    """第1题：传入姓名，返回 "XX 你好"。"""
    return name + " 你好"


def cal(a, b, op="+"):
    """第2题：带默认参数的计算器，op 不传时默认做加法。"""
    if op == "+":
        return a + b
    return a - b


def total(*args):
    """第3题：用 *args 接收任意个数字，返回它们的和。"""
    return sum(args)


def main():
    print(hello("张三"))  # 张三 你好

    print(cal(10, 3))  # 13
    print(cal(10, 3, "-"))  # 7

    print(total(1, 2, 3, 4))  # 10


if __name__ == "__main__":
    main()
