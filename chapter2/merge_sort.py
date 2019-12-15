"""
归并排序
----------
算法原理：
    要将一个数组排序，可以先（递归的）将它分成两半排序，然后将结果合并起来
----------
时间复杂度：O(NlogN)
----------
改良：
    1.对小规模数组采取插入排序
    2.测试数组是有序：判断a[mid]是否小于等于a[mid+1], 如果是，我们直接判断数组有序了

"""
from sort_base import SortBase
class MergeSort1(SortBase):
    """
    自顶向下的归并排序
    """
    def __init__(self, arr):
        super(MergeSort1, self).__init__(arr)

    def sort(self):
        self.merge_sort(0, self.length-1)
        
    def merge_sort(self, low, high):
        if low < high:
            mid = low + (high - low)// 2
            self.merge_sort(low, mid)
            self.merge_sort(mid+1, high)
            self.merge(low, high)
        
    def merge(self, low, high):
        """
        将[lwo,mid] 与[mid+1,high]归并
        """
        mid = low + (high - low)// 2
        aux = self.arr[low:high+1].copy() #辅助数组
        i = low
        j = mid + 1
        k = low
        for k in range(low, high+1):
            if i > mid:
                self.arr[k] = aux[j-low]
                j += 1
            elif j > high:
                self.arr[k] = aux[i-low]
                i += 1
            elif aux[j-low] < aux[i-low]:
                self.arr[k] = aux[j-low]
                j += 1
            else:
                self.arr[k] = aux[i-low]
                i += 1
 
class MergeSort2(SortBase):
    """
    自底向上的原地归并
    """
    def __init__(self, arr):
        super(MergeSort2, self).__init__(arr)

    def sort(self):
        sz = 1
        while sz < self.length:
            lo = 0
            while lo < self.length - sz:
                self.merge(lo, lo+sz-1, min(lo+2*sz-1, self.length-1))
                lo += 2 * sz
            sz = 2 * sz

    def merge(self, low, mid, high):
        """
        将[lwo,mid] 与[mid+1,high]归并
        """
        aux = self.arr[low:high+1].copy() #辅助数组
        i = low
        j = mid + 1
        k = low
        for k in range(low, high+1):
            if i > mid:
                self.arr[k] = aux[j-low]
                j += 1
            elif j > high:
                self.arr[k] = aux[i-low]
                i += 1
            elif aux[j-low] < aux[i-low]:
                self.arr[k] = aux[j-low]
                j += 1
            else:
                self.arr[k] = aux[i-low]
                i += 1
 



def test():
    arr_test = [12, 11, 13, 5, 6, 7] 
    a = MergeSort2(arr_test)
    a.sort()
    a.show() 
if __name__ == "__main__":
    test()
