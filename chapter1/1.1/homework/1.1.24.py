#encoding=utf-8
"""
给出使用欧几里得算法计算105和24的最大公约数的过程中得到的一系列p和q值
扩展得到Eculid程序， 从命令行得到两个参数，计算他们的最大公约出并打印出每次递归调用是的两个参数
计算1111111和1234567的最大公约数
"""

import argparse

def Eculid(x, y):

    p, q = max(x, y), min(x, y)
    if q == 0:
        print(p, q)
        return p
    print(q, p%q)
    return Eculid(q, p%q)


if __name__ == "__main__":
    print(Eculid(105, 24))
    print(Eculid(1111111, 1234567))
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int)
    parser.add_argument('y', type=int)
    args = parser.parse_args()
    x = args.x
    y = args.y
    print(Eculid(x, y))

