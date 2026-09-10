"""自写工具模块：提供 max3，被 包与模块练习.py 导入使用。"""


def max3(a, b, c):
    """返回 a、b、c 三个数中的最大值。"""
    biggest = a  # 先假设第一个数最大
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest
