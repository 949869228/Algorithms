#coding=utf-8
"""
编写一个静态方法histogram(), 接受一个整形数组a与一个整数M为参数并返回一个大小为M的数组，
其中第i个元素的值为整数i在参数数组中出现的次数。如果a中的值均在0到M-1之间，返回元素中所有
元素之和应该和a.length相等
"""

def histogram(a, M):
    result = [0] * M
    for i in a:
        if i > M-1:
            raise ValueError("elements in a should less than M")
        result[i] += 1
    return result

if __name__ == "__main__":
    print(histogram([1,2,2,3,5],6))