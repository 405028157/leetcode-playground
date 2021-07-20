import random

def partition(A: list[int], left: int, right: int):
    i, j = left, right

    while i < j:
        # 这里一定要先处理j，不能先处理i
        while i < j and A[j] >= A[left]:
            j -= 1
        while i < j and A[i] <= A[left]:
            i += 1
        
        A[i], A[j] = A[j], A[i]
    
    A[i], A[left] = A[left], A[i]
    return i

def partition_random(A: list[int], left: int, right: int):
    index = random.randint(left, right)
    A[index], A[left] = A[left], A[index]
    i, j = left, right

    while i < j:
        while i < j and A[j] >= A[left]:
            j -= 1
        while i < j and A[i] <= A[left]:
            i += 1
        
        A[i], A[j] = A[j], A[i]
    
    A[i], A[left] = A[left], A[i]
    return i

def quickSort(A: list[int], left: int, right: int):
    if left < right:
        pos = partition_random(A, left, right)
        quickSort(A, left, pos - 1)
        quickSort(A, pos + 1, right)


A = [9,5,2,13,7,15]
quickSort(A, 0, 5)
print(A)