# coding=utf-8
# 编写一段代码，打印出一个M行N列二维数组的转置（交换行和列）
def transpose(arr):
    """
    arr is a list
    """
    M = len(arr)
    N = len(arr[0])
    result = []
    for i in range(N):
        rows = []
        for j in range(M):
            rows.append(arr[j][i])
        result.append(rows)
    return result

if __name__ == "__main__":
    print(transpose([[1, 2, 3], [4, 5, 6]]))