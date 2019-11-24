
class sort_base():
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
    
    def isSorted(self):
        """
        判断数组是否有序(升序)
        """
        for i in range(self.length-1):
            if not self.__less(i, i+1):
                return False
        return True

class sort_selection(sort_base):
    def __init__(self, arr):
        super(sort_selection, self).__init__(arr)
    
    def sort(self):
        for i in range(self.length-1):
            min_index = i
            for j in range(i+1, self.length):
                if self.less(j, min_index):
                    self.exchange(j, min_index)

    def test(self):
        arr_test = [1, 3, 7, 4, 2]
        a = sort_selection(arr_test)
        a.sort()
        a.show()

class sort_insertion(sort_base):
    def __init__(self, arr):
        super(sort_insertion, self).__init__(arr)

    def sort(self):
        for i in range(1, self.length):
            j = i
            while j > 0 and self.less(j, j- 1):
                self.exchange(j-1, j)
                j -= 1

    def test(self):
        arr_test = [1, 3, 7, 4, 2]
        a = sort_insertion(arr_test)
        a.sort()
        a.show()

