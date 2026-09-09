"""练习3（追加）：用 a 模式追加一个同学，再读一遍确认 4 个人都在。

a 模式在文件末尾追加内容，不会覆盖已有内容。
"""

from pathlib import Path

FILE_NAME = Path(__file__).with_name("class_list.txt")


def main():
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write("赵六" + "\n")
    print("已追加 赵六")

    # 再读一遍，确认 4 个人都在
    with open(FILE_NAME, encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
    print(f"现在名单里共 {len(names)} 个人：{names}")


if __name__ == "__main__":
    main()
