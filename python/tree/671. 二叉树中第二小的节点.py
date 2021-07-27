import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return None

        q = collections.deque([root])
        l = []
        
        while q:
            top = q.pop()
            l.append(top.val)
            
            # 有就是俩个孩子 所以只判断top.left就行
            if top.left:
                q.append(top.left)
                q.append(top.right)

        l.sort()

        minValue = l[0]
        for i in range(1, len(l)):
            if l[i] > minValue:
                return l[i]
        
        return -1
