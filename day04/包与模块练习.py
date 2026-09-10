"""包与模块练一练：random 抽人、datetime 打印日期、自写模块 我的工具模块。"""

import random
from datetime import date

from 我的工具模块 import max3

NAMES = ["小明", "小红", "小刚", "小美", "小强"]

# date.weekday() 返回 0~6，0 是星期一，用它当下标取中文星期
WEEKDAYS = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


def practice1():
    """练习1（random）：随机抽一位同学。"""
    print(f"抽中的同学：{random.choice(NAMES)}")


def practice2():
    """练习2（datetime）：打印今天的日期。"""
    today = date.today()
    print(f"{today:%Y年%m月%d日} {WEEKDAYS[today.weekday()]}")


def practice3():
    """练习3（自写模块）：使用 my_utils 里的 max3。"""
    print(f"max3(3, 9, 5) = {max3(3, 9, 5)}")


def challenge():
    """挑战·三合一：随机抽人 + 打印抽中的人 + 打印今天是星期几。"""
    chosen = random.choice(NAMES)
    print(f"抽中的同学：{chosen}，今天是{WEEKDAYS[date.today().weekday()]}")


def main():
    practice1()
    practice2()
    practice3()
    challenge()


if __name__ == "__main__":
    main()
