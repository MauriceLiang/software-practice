"""练习1（loads）：解析一段 AI 返回的 JSON 文本，取出里面的 content。"""

import json


def main():
    # 模拟 AI 接口返回的 JSON 文本（注意：外层是字符串，里面的引号是双引号）
    text = '{"choices": [{"message": {"content": "你好"}}]}'

    # loads: 把 JSON 字符串解析成 Python 字典/列表
    data = json.loads(text)

    # 逐层取值：choices -> 第一个 -> message -> content
    content = data["choices"][0]["message"]["content"]
    print(content)


if __name__ == "__main__":
    main()
