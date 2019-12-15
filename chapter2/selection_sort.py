"""
选择排序
----------
算法原理：
    首先找到数组中最小的那个元素，其次将它和数组中第一个元素交换位置。再次，在剩下的元素中找到最小的元素，将其余第二个 元素交换位置。如此往复，直到将整个数组排序
----------
空间复杂度：O(1)
时间复杂度：O(N^2)
----------
特点：
1.运行时间和输入无关
2.数组移动是最少的：N次
---------
和冒泡排序的区别：每次记录min索引值而非交换位置
"""
from sort_base import SortBase
class SelectionSort(SortBase):
    def __init__(self, arr):
        super(SelectionSort, self).__init__(arr)

    def sort(self):
        for i in range(self.length-1):
            min_index = i
            for j in range(i+1, self.length):
                if self.less(j, min_index):
                    self.exchange(j, min_index)

def test():
    arr_test = [1, 3, 7, 4, 2]
    a = SelectionSort(arr_test)
    a.sort()
    a.show() 
if __name__ == "__main__":
    test()
