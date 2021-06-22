class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        path = []

        def dfs(node: TreeNode, sum):
            if not(node.left or node.right) and sum == node.val:
                res.append(path + [node.val])
            
            path.append(node.val)
            
            if node.left:
                dfs(node.left, sum - node.val)
            
            if node.right:
                dfs(node.right, sum - node.val)
            
            path.pop()
        
        dfs(root, targetSum)

        return res