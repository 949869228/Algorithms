"""
堆有序：当一颗二叉树能够很好的

"""

class Heap:
    """
    二叉堆

    二叉堆是一组能够用堆有序的完全二叉树排序的元素，并在数组中按照层级储存
    堆有序：二叉树的每一个节点都大于等于它的两个子节点。根节点是堆有序的二叉树中的最大节点

    """
    def __init__(self, arr):
        self.arr = [0]
        for i in arr:
            self.insert(i)

    def __exchange(self, i, j):
        """
        交换两个元素
        """
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
    
    def __less(self, i, j):
        """
        比较两个元素的大小
        """
        if self.arr[i] < self.arr[j]:
            return True
        return False
    
    def swim(self, k):
        """
        由下至上的堆有序化。
        """
        while k > 1 and self.__less(k//2, k):
            self.__exchange(k//2, k)
            k = k// 2

    def sink(self, k):
        """
        如果堆的有序状态因为某个节点变得比它的两个子节点或是其中之一更小了而被打破了
        就可以铜鼓欧将它和它的两个子节点中的较大者交换来恢复堆
        """
        while 2 * k <= len(self.arr):
            j = 2 * k
            if j < N and self.__less(j, j+1):
                j += 1
            if not self.__less(k, j):
                break
            self.__exchange(k, j)
            k = j
    
    def insert(self, v):
        """
        插入某个元素
        """
        self.arr.append(v)
        k = len(self.arr) - 1
        self.swim(k)

    def del_max(self):
        """
        删除最大元素
        """
        end_index = len(self.arr)
        self.__exchange(1, end_index)
        self.arr.pop(-1)
        self.sink(1)
if __name__ == "__main__":
    arr = [1, 3, 7, 4, 2, 1, 3, 5, 0, 13]
    a = Heap(arr)
    print(a.arr)

