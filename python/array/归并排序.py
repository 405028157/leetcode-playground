def merge(A: list[int], left:int, mid: int, right: int):
    # 合并A[left], ..., A[mid] 和 A[mid + 1], ..., A[right] 俩个有序序列
    i, j = left, mid + 1
    temp = []

    while i <= mid and j <= right:
        if A[i] < A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    
    while i <= mid:
        temp.append(A[i])
        i += 1
    
    while j <= right:
        temp.append(A[j])
        j += 1
    
    for i in range(left, right + 1):
        A[i] = temp[i - left]

def mergeSort(A: list[int], left: int, right: int):
    if left < right:
        mid = (left + right) >> 1
        mergeSort(A, left, mid)
        mergeSort(A, mid + 1, right)
        merge(A, left, mid, right)

A = [9,5,2,13,7,15]
mergeSort(A, 0, 5)
print(A)