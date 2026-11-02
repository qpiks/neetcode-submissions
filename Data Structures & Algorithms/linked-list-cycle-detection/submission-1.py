# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        i = 0
        slow, fast = head, head.next
        while fast:
            if slow == fast:
                return True
            if i % 2 == 1:
                slow = slow.next
                i = 1       
            fast = fast.next
            i += 1
        return False

        