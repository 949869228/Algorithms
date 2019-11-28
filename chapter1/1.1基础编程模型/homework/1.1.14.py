#coding=utf-8
"""
编写一个静态方法lg()， 接受一个整形参数N， 返回不大于log2N的最大整数，不要使用math库
"""

def lg(N):
    i = 0
    while 2**(i+1) < N:
        i += 1
    return i


if __name__ == "__main__":
    print(lg(100000000))