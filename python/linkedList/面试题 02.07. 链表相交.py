# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1, cur2 = headA, headB
        
        while cur1 != cur2:
            cur1 = cur1.next if cur1 != None else headB
            cur2 = cur2.next if cur2 != None else headA
        
        return cur1
        