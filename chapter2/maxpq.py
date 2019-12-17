"""
优先队列
----------
最重要的操作：
    删除最大元素和插入元素
应用：
    模拟系统，任务调度，数值计算

"""
class MaxPQ:
    """
    内存保存元素可以基于有序数组，无需数组，以及链表
    这里展示基于无序数组的优先队列
    """
    def __init__(self, arr=[], max_length=None):
        self.arr = arr
        self.max_length = max_length
        if self.max_length is not None:
            if len(self.arr) > self.max_length:
                raise Exception("The array length beyond the max support")
    
    def insert(self, v):
        """
        向优先队列中插入一个元素
        """
        if len(self.arr) == self.max_length:
            raise Exception("the array reaches the max length , please delete some elements")
        self.arr.append(v)

    def max(self):
        """
        返回最大元素
        """
        length = len(self.arr)
        max_index = 0
        for i in range(1, length):
            if self.arr[i] > self.arr[max_index]:
                max_index = i
        return self.arr[max_index]

    def del_max(self):
        """
        删除并返回最大元素
        """
        length = len(self.arr)
        max_index = 0
        for i in range(1, length):
            if self.arr[i] > self.arr[max_index]:
                max_index = i
        max_value = self.arr[max_index]
        self.arr.pop(max_index)
        return max_value

    def is_empty(self):
        """
        返回队列是否为空
        """
        if self.arr == []:
            return True
        return False

    def size(self):
        """
        返回优先队列中元素的个数
        """
        return len(self.arr)

if __name__ == "__main__":
    arr = [1, 7, 11, 9, 15, 23]
    ss = MaxPQ(arr)
    print(ss.max())
    ss.del_max()
    print(ss.max())
    ss.insert(100)
    print(ss.max())
    print(ss.size())