# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dic = {}
        res = []

        def dfs(node: TreeNode):
            if not node:
                return
            
            if node.left:
                dic[node.left] = node
            if node.right:
                dic[node.right] = node
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        visited = {}
        # 对于出发点target，到另一个node，只可能有一种路径和对应的一个distance，因此访问过一个节点，就不用去访问了
        def search(node: TreeNode, distance: int):
            visited[node] = True # 这里也可以让节点值作为key，因为树的每个节点值都不同

            if distance == k:
                res.append(node.val)
                return
            
            if not visited[node.left]:
                search(node.left, distance + 1)
            if not visited[node.right]:
                search(node.right, distance + 1)
            if not visited[dic[node]]:
                search(dic[node], distance + 1)
        
        search(target, 0)
        return res
        

            