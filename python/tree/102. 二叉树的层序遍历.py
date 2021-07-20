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
        q = collections.deque()
        res = []
        
        q.append(root)

        while q:
            cur_layer = []
            for _ in range(len(q)):
                cur = q.popleft()
                cur_layer.append(cur.val)
                cur.left and q.append(cur.left)
                cur.right and q.append(cur.right)
            # 这里确实可以不切片
            res.append(cur_layer)
        
        return res
                

