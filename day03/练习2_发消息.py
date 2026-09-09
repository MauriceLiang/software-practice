"""练习2（dumps）：把一条消息字典转成 JSON 文本并打印。"""

import json


def main():
    # 要发送的消息
    message = {"role": "user", "content": "今天天气怎么样"}

    # dumps: 把 Python 字典转成 JSON 字符串
    # ensure_ascii=False: 保留中文（默认会把中文转成 \uXXXX 转义）
    # indent=2: 缩进 2 格，打印出来更易读
    text = json.dumps(message, ensure_ascii=False, indent=2)
    print(text)


if __name__ == "__main__":
    main()
