"""
编写一段代码，将一个正整数N用二进制表示并转化为一个string类型的值s
"""

def int2sting(N):
    if not isinstance(N, int):
        raise TypeError("N must be an int")
    return str(bin(N))


if __name__ == "__main__":
    print(int2sting(22))

"""
附：python各个进制之间的转换
-------------------------------
# 二进制 to 十进制: int(str,n=10) 
# 十六进制 to 十进制: int(str, 16)
# 十进制 to 二进制: bin() 
# 十进制 to 八进制: oct() 
# 十进制 to 十六进制: hex() 
其他进制之间的转换可通过与十进制间的转化实现
"""
