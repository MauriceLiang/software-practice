"""课堂练习·综合四题：去重、嵌套遍历、random+os、datetime。"""

import os
import random
from datetime import date
from pathlib import Path

# 名单文件与本脚本放在同一目录
NAME_FILE = Path(__file__).with_name("名单.txt")

NAMES = ["小明", "小红", "小刚", "小美", "小强"]

# date.weekday() 返回 0~6，0 是星期一，用它当下标取中文星期
WEEKDAYS = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

# 练习2 用的消息列表：列表里套字典
MESSAGES = [
    {"role": "user", "content": "什么是列表？"},
    {"role": "assistant", "content": "列表是可变的有序序列，用中括号写。"},
    {"role": "user", "content": "那元组呢？"},
]


def practice1():
    """练习1（去重）：words 列表有重复，用 set 去重后打印个数。"""
    words = ["python", "json", "python", "set", "json", "python"]
    print(f"去重前 {len(words)} 个，去重后 {len(set(words))} 个")


def practice2():
    """练习2（嵌套遍历）：遍历 messages，打印每条的 role 和 content。"""
    for message in MESSAGES:
        print(f'{message["role"]}: {message["content"]}')


def practice3():
    """练习3（random+os）：随机抽一位同学，并检查 名单.txt 是否存在。"""
    print(f"抽中的同学：{random.choice(NAMES)}")
    if os.path.exists(NAME_FILE):
        print("名单.txt 存在")
    else:
        print("名单.txt 不存在")


def practice4():
    """练习4（datetime）：打印今天的日期，并判断是不是周六日。"""
    today = date.today()
    print(f"{today:%Y年%m月%d日} {WEEKDAYS[today.weekday()]}")
    if today.weekday() >= 5:  # 5 是星期六，6 是星期日
        print("今天是周六日")
    else:
        print("今天不是周六日")


def main():
    practice1()
    practice2()
    practice3()
    practice4()


if __name__ == "__main__":
    main()
