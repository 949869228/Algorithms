"""
插入排序
----------
算法原理：
    
----------
空间复杂度：O(1)
时间复杂度：O(N^2)
----------
对部分有序数组很有效，也很适合小规模数组
"""
from sort_base import SortBase
class InsertionSort(SortBase):
    def __init__(self, arr):
        super(InsertionSort, self).__init__(arr)


    def sort(self):
        for i in range(1, self.length):
            j = i
            while j > 0 and self.less(j, j-1):
                self.exchange(j-1, j)
                j -= 1

def test():
    arr_test = [1, 3, 7, 4, 2, 1, 3, 5, 0, 13]
    a = InsertionSort(arr_test)
    a.sort()
    a.show() 

if __name__ == "__main__":
    test()
