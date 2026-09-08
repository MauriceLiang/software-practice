"""数据类型和字符串转换练习。"""


def main():
    name = "梁渊玮"
    age = 20
    value = 99.99
    has_car = None
    number_list = [1, 2, 3]
    number_tuple = (1, 2, 3)
    is_married = False

    print(f"name 的类型：{type(name)}")
    print(f"age 的类型：{type(age)}")
    print(f"value 的类型：{type(value)}")
    print(f"has_car 的类型：{type(has_car)}")
    print(f"number_list 的类型：{type(number_list)}")
    print(f"number_tuple 的类型：{type(number_tuple)}")
    print(f"is_married 的类型：{type(is_married)}")

    number_text = "100"
    number = int(number_text)
    print(f"字符串转换成整数后：{number + 200}")


if __name__ == "__main__":
    main()
