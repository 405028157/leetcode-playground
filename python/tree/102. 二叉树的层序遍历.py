import collections
"""
此题也可以不用俩个q1, q2，用一个q，在第二层遍历的时候，利用一下队列的长度
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        q1 = collections.deque()
        q2 = collections.deque()
        res = []
        
        q1.append(root)

        while q1:
            cur_layer = []
            while q1:
                cur = q1.popleft()
                cur_layer.append(cur.val)
                cur.left and q2.append(cur.left)
                cur.right and q2.append(cur.right)
            res.append(cur_layer)
            q1, q2 = q2, q1
        
        return res
                

