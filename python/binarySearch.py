# 二分查找总结 https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
"""
二分法 定义 target 是在一个在左闭右闭的区间里，即[left, right]
"""

A = [1, 2, 3, 4, 10]
def binarySearch(A, target):
    start, end = 0, len(A) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if A[mid] < target: 
            start = mid + 1 # 既然A[mid]不等target，就不要留恋，无论start和end，都不要取这个值了，这样才能迅速逼近范围
        elif A[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1


"""
二分法 定义 target 左闭右开的区间里，也就是[left, right)
这种写法有个好处，循环结束的时候一定有left == right
"""
A = [1, 2, 3, 4, 10]
def binarySearch2(A, target):
    start, end = 0, len(A)
    while start < end:
        print(f'start={start}, end={end}')
        mid = int((start + end) / 2)
        if A[mid] < target: 
            start = mid + 1 # 既然A[mid]不等target，就不要留恋，无论start和end，都不要取这个值了，这样才能迅速逼近范围
        elif A[mid] > target:
            end = mid # 下一次循环区间在[start, end)，不包含end
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(binarySearch2(A, 10))
