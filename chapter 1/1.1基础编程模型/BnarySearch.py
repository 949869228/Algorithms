"""
Description：二分查找的递归实现
Author：larryhe
date:2019.08.10
"""

def binary_search(target, arr, lo, hi):
    """
    parameter：
        target：the number you want to Find 
        arr: the array, a list 
    returns:
        y:the index that target in arr,if not in ,return -1
    """
    if lo > hi:
        return -1
    if target < arr[lo] or target > arr[hi]:
        return -1
    mid = lo + (hi - lo)//2
    if target < arr[mid]:
        return binary_search(target, arr[:], lo, mid-1)
    elif target > arr[mid]:
        return binary_search(target, arr[:], mid+1, hi)
    else:
        return mid

if __name__ == "__main__":
    print(binary_search(5, [1,5,7], 0, 2))