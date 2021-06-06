class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 一遍遍历，边写字典边找答案，可行的原因是若有a+b=target，那么也有b+a=target，如果先遍历到a，没找到dic[target-a]，此时在字典添加dic[a] = someIndex，遍历到b时，就可以找到dic[target-b]
        dic = {}
        for idx, value in enumerate(nums):
            if target - value in dic:
                return [dic[target-value], idx]
            dic[value] = idx
            