# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        last = None
        cur = head
        while cur: # 尽可能拿浅显和直接的变量当做循环的条件... 但是循环结束cur是None，应该返回last
            nxt = cur.next
            cur.next = last
            last = cur
            cur = nxt
        return last