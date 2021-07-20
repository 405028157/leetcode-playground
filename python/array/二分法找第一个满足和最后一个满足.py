"""
1、 l, r = 0, len(nums) - 1
2、 若一直找不到满足条件的值，l最终可以达到len(nums)，r最终可以达到-1
3、 搜索区间是[l, r]，对于while条件是 l <= r
4、 如果是找第一个满足条件，就盯着l，如果是找最后一个满足条件，就盯着r
"""

def findFirstPosition(nums, target):
    l, r = 0, len(nums) - 1

    # [l, r]
    while l <= r:
        mid = (l + r) >> 1
        print(f'mid = {mid}')
        if nums[mid] == target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    if l >= len(nums) or nums[l] != target:
        return -1
    
    return l

def findLastPosition(nums,target):
    l, r = 0, len(nums) - 1

    # [l, r]
    while l <= r:
        mid = (l + r) >> 1

        if nums[mid] == target:
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    if r == -1 or nums[r] != target:
        return -1
    
    return r

ret = findFirstPosition([1,2,9,11,13,15], 9)
print(ret)

# ret2 = findLastPosition([1,2,3,4,9,9,9,11], 9)
# print(ret2)


"""
nums = [1,2,3,4,9,9,9,11] 找 12

l = 0 r = 7 mid = 3
l = 4 r = 7 mid = 5
l = 6 r = 7 mid = 6
l = 7 r = 7 mid = 7
l = 8 r = 7 

nums[7] != 12

nums = [1,2,3,4,9,9,9,11] 找 0
l = 0 r = 7 mid = 3
l = 0 r = 2 mid = 1
l = 0 r = 0 mid = 0
l = 0 r = -1 

r == -1
"""