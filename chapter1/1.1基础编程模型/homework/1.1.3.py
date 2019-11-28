"""
description：编写一个程序，从命令行得到三个整数，如果他们都相等则打印equal，否则打印not
argparse官方文档：https://docs.python.org/3/library/argparse.html#module-argparse
"""
import argparse
def main():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('x', type=int)
    parser.add_argument('y', type=int)
    parser.add_argument('z', type=int)
    args = parser.parse_args()
    x = args.x
    y = args.y
    z = args.z
    if x == y and y == z:
        print("equal")
    else:
        print("not equal")

if __name__ == '__main__':
    main()

"""
命令行运行
python 1.1.3.py 1 1 1
即可
"""