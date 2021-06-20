import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            layer_value = 0
            for _ in range(len(q)):
                node = q.popleft()
                layer_value = node.val
                node.left and q.append(node.left)
                node.right and q.append(node.right)
            res.append(layer_value)
        
        return res