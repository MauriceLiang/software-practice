"""练习1（写文件）：把 3 个同学名字写进名单。

w 模式会覆盖文件原有内容；每个名字结尾写 \\n 实现换行。
"""

from pathlib import Path

# 名单文件与本脚本放在同一目录，避免受运行目录影响
FILE_NAME = Path(__file__).with_name("class_list.txt")


def main():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for name in ["张三", "李四", "王五"]:
            f.write(name + "\n")
    print("已把 3 个同学的名字写入 class_list.txt，每个名字一行")


if __name__ == "__main__":
    main()
