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
        while c1 and c2:
            n = c1.val + c2.val + carry
            curr.next = ListNode(n % 10)
            carry = n // 10
            c1, c2, curr = c1.next, c2.next, curr.next
        while c1:
            n = c1.val + carry
            curr.next = ListNode(n % 10)
            carry = n // 10
            c1, curr = c1.next, curr.next
        while c2:
            n = c2.val + carry
            curr.next = ListNode(n % 10)
            carry = n // 10
            c2, curr = c2.next, curr.next
        if carry:
            curr.next = ListNode(carry)
        return head



        