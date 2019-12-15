"""
希尔排序
----------
算法原理：
    使数组中任意间隔为h的元素都是有序的
----------

"""
from sort_base import SortBase
class ShellSort(SortBase):
    def __init__(self, arr):
        super(ShellSort, self).__init__(arr)

    def sort(self):
        h = 1
        while (h < self.length//3):
            h = 3 * h + 1
        while h >= 1:
            # 将数组变为h有序
            for i in range(h, self.length):
                j = i
                while j >= h and self.less(j ,j-h):
                    # 将i插入到i-h i-2*h...后面
                    self.exchange(j, j-h)
                    j -= h
            h = h // 3



def test():
    arr_test = [1, 3, 7, 4, 2]
    a = ShellSort(arr_test)
    a.sort()
    a.show() 
if __name__ == "__main__":
    test()
