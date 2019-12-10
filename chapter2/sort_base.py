class SortBase:
    """
    排序算法的基类
    """
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    def less(self, i, j):
        """
        判断array i < array j
        """
        return self.arr[i] < self.arr[j]

    def exchange(self, i, j):
        """
        交换i,j的值
        """
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def show(self):
        """
        单行打印数组元素
        """
        print(self.arr)
    
    def issorted(self):
        """
        判断数组是否有序（升序）
        """
        for i in range(self.length):
            if not self.less(i, i+1):
                return False
        return True
