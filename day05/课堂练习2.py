"""课堂练习②·面向对象两题：Dog 类，以及 Cat 继承 Dog 并重写 bark。"""


class Dog:
    """第1题：Dog 类，数据是名字 name，方法 bark() 打印 "汪汪"。"""

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "汪汪!")


class Cat(Dog):
    """第2题：Cat 继承 Dog，但猫不会汪汪，所以在 Cat 里重写 bark。"""

    def bark(self):
        print(self.name, "喵喵!")


def main():
    d = Dog("旺财")
    d.bark()  # 旺财 汪汪!

    c = Cat("咪咪")
    c.bark()  # 咪咪 喵喵!


if __name__ == "__main__":
    main()
