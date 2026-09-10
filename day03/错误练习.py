"""错误处理练一练：try 包住可能出错的代码，except 接住，程序不崩。"""

import json
from pathlib import Path

# 配置文件与本脚本放在同一目录
CONFIG_FILE = Path(__file__).with_name("config.json")


def practice1():
    """练习1（文件防崩）：读不存在的文件。"""
    try:
        with open("不存在.txt", encoding="utf-8") as f:
            content = f.read()
        print(content)
    except FileNotFoundError:
        print("文件不存在")
    # 走到这里说明异常已经被接住，没有往上抛
    print("程序没有崩")


def practice2():
    """练习2（JSON 防崩）：解析坏文本。"""
    try:
        data = json.loads("这不是JSON")
        print(data)
    except json.JSONDecodeError:
        print("格式不对")


def practice3():
    """练习3（挑战·三合一）：从 config.json 读 JSON 取 api_key，全程防崩。"""
    try:
        with open(CONFIG_FILE, encoding="utf-8") as f:
            config = json.load(f)
        print(config["api_key"])
    except FileNotFoundError:
        print("文件不存在，读取失败")
    except KeyError:
        print("配置里没有 api_key 这个键")
    except Exception as e:  # 兜底：其他没预料到的错误也不让程序崩
        print(f"其他错误：{e}")


def main():
    practice1()
    practice2()
    practice3()


if __name__ == "__main__":
    main()
