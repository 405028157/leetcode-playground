# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        max_depth = 0

        # 因为总是先左后右，所以到达某层的时候肯定是最左边的节点
        def dfs(node: TreeNode, depth: int):
            nonlocal max_depth
            # 到达叶子节点
            if not(node.left or node.right):
                # 每层只要一个值
                if depth > max_depth:
                    self.ans = node.val
                    max_depth = depth
            
            if node.left:
                dfs(node.left, depth + 1)
            
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.ans
        