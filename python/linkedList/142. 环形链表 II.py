# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        step = 0
        slow = head
        fast = head.next
        while fast and slow != fast:
            print(step)
            step += 1
            slow = slow.next
            fast = fast.next and fast.next.next
        
        # 退出循环有俩种情况，fast = None, 或者 slow == fast
        if not fast:
            return None
        
        # print(step)
        cur = head
        print(step)
        for _ in range(step):
            cur = cur.next
        
        return cur