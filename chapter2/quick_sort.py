"""
快速排序
----------
算法原理：
    
----------
特点：
    1.原地排序
    2.时间NlogN
缺点：
    非常脆弱，在实现时需要非常小心才能避免低劣的性能
----------
快排与归并：
    归并：将数组分成连个子数组分别排序，并将有序的子数组归并以使得整个数组有序--递归调用发生在处理整个数组之前
        --数组被等分为两半
    快排：当两个子数组有序时，整个数组自然有序了--递归调用发生在处理整个数组之后
        --切分位置取决于数组内容
----------
算法改进：
    1.对于小数组，切入到插入排序
    2.三取样切分：使用子数组的一小部分的元素的中位数来切分数组
    3.熵最优排序：将数组切分为三部分，分别对应大于，等于和小于（一个元素全部重复的子数组就无需排序了）
"""
from sort_base import SortBase
import random

class QuickSort(SortBase):
    """
    快速排序
    """
    def __init__(self, arr):
        super(QuickSort, self).__init__(arr)

    def sort(self):
        random.shuffle(self.arr)
        self.quick_sort(0, self.length-1)
        
    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition2(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)

    def partition(self, low, high):
        """
        功能：每次将切分元素放在合适的位置上
        选择a[low]作为切分元素，从左至右扫描找到第一个大于它的数，从右至左扫描找到第一个小于它的数，然后两者交换位置。
        这个过程并不保证稳定排序
        """
        pivot = self.arr[low]
        i = low + 1
        j = high
        while True:
            while self.less(i, low):
                if i == high:
                    break
                i += 1
            while self.less(low, j):
                if j == low:
                    break
                j -= 1
            if i >= j:
                break
            self.exchange(i, j)
        self.exchange(low, j)
        return j
    
    def partition2(self, low, high):
        """
        i标识的位置是左数组尾部的索引，循环过程就是不断将小数字移动到左边
        解释详见：https://blog.csdn.net/uestc_my/article/details/45600499
        """
        i = low - 1
        pivot = self.arr[high]
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[j+1] = self.arr[j+1], self.arr[i+1]
        return i + 1


class QuickSort2(SortBase):
    """
    三向切分的快速排序
    """
    def __init__(self, arr):
        super(QuickSort2, self).__init__(arr)

    def sort(self):
        random.shuffle(self.arr)
        self.quick_sort(0, self.length-1)
        
    def quick_sort(self, low, high):
        if low < high:
            lt = low
            i = low + 1
            gt = high
            v = self.arr[low]
            while i <= gt:
                if self.arr[i] < v:
                    self.exchange(lt, i)
                    lt += 1
                    i += 1
                elif self.arr[i] > v:
                    self.exchange(i, gt)
                    gt -= 1
                else:
                    i += 1
            self.quick_sort(low, lt-1)
            self.quick_sort(gt+1, high)


def test():
    arr_test = [12, 11, 13, 5, 6, 7] 
    a = QuickSort2(arr_test)
    a.sort()
    a.show() 
if __name__ == "__main__":
    test()
