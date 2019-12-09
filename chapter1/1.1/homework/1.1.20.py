#coding=utf-8
"""
编写一个递归的静态方法计算ln(N!)的值
"""
import math
def ln(n):
    if n == 1:
        return 0
    return math.log(n) +ln(n-1)

if __name__ == "__main__":
    print(ln(5))
    print(math.log(120))