# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(A: TreeNode, B: TreeNode):
            if not B: return True
            if not A: return False
            if A.val != B.val: return False
            return dfs(A.left, B.left) and dfs(A.right, B.right)

        return bool(A and B) and (dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))








"""
[4,2,3,4,5,6,7,8,9]
[4,8,9]

                                        node1 = TreeNode{val: 4,
                        left: TreeNode{val: 2,
                left: TreeNode{val: 4,
        left: TreeNode{val: 8,
left: None, right: None}, right: TreeNode{val: 9,
                        left: None, right: None}}, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}

测试用例没过，问题在于题目没有保证节点的值唯一，所以findNode中用cur.val == target.val判断，在A中找到的第一个符合条件的节点，不一定是正确的B的根节点。
"""
# class Solution:
#     def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
#         if not B:
#             return False
        
#         startNode = self.findNode(A, B)
#         if not startNode:
#             return False
        
#         def dfs(node1: TreeNode, node2: TreeNode):
#             if not(node1 or node2):
#                 return True
#             if not (node1 and node2):
#                 return False
            
#             if node1.val != node2.val:
#                 return False
            
#             return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
#         return dfs(startNode, B)
    
#     def findNode(self, cur: TreeNode, target: TreeNode):
#         if not cur:
#             return False
        
#         if cur.val == target.val:
#             return cur
        
#         return self.findNode(cur.left, target) or self.findNode(cur.right, target)