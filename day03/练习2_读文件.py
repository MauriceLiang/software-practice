"""练习2（读文件）：逐行读取并打印名单。

with 会自动关闭文件；for line in f 逐行读出，strip() 去掉每行末尾的换行符。
"""

from pathlib import Path

FILE_NAME = Path(__file__).with_name("class_list.txt")


def main():
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f:
            print(f"  {line.strip()}")


if __name__ == "__main__":
    main()
