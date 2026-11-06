# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        c1, c2 = l1.next, l2.next
        curr = head
        print(head.val)
        while c1 or c2 or carry != 0:
            if c1:
                v1 = c1.val
                c1 = c1.next
            else:
                v1 = 0
            if c2:
                v2 = c2.val
                c2 = c2.next
            else:
                v2 = 0
            n = v1 + v2 + carry
            curr.next = ListNode(n % 10)
            carry = n // 10
            curr = curr.next
        
        return head



        