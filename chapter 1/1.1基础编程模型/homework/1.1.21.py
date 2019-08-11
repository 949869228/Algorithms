#coding=utf-8
"""
编写一段程序，从标准输入中按行读取数据， 其中每行都包括一个名字和两个整数。然后，
用print打印一张表格， 每行的若干列包括名字、两个整数和第一个整数除以第二个整数的
结果，结果精确到小数点后三位
"""

if __name__ == "__main__":
    data = input().split("/n")
    for i in data:
        name, x, y, = i.split()
        print(name, x, y, '%.3f'%(float(x)/int(y)))