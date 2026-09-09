"""练习3（挑战）：从 JSON 文件读取配置，取出 api_key 打印。"""

import json
from pathlib import Path

# 配置文件与本脚本放在同一目录
CONFIG_FILE = Path(__file__).with_name("config.json")


def main():
    # 先写一个配置文件（实际项目里由部署/发布环节提供）
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"api_key": "sk-abc123"}, f)

    # load: 从文件对象直接读 JSON（和 loads 的区别：load 传文件对象，loads 传字符串）
    with open(CONFIG_FILE, encoding="utf-8") as f:
        config = json.load(f)

    print(config["api_key"])


if __name__ == "__main__":
    main()
