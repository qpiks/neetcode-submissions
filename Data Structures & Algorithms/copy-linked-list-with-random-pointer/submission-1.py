"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node(head.val)
        curr = head.next
        new_curr = new_head
        pointers = {head: new_head}
        while curr:
            new_node = Node(curr.val)
            pointers[curr] = new_node
            new_curr.next = new_node
            new_curr = new_curr.next
            curr = curr.next

        new_curr = new_head
        curr = head
        while curr:
            new_curr = pointers[curr]
            new_curr.random = pointers.get(curr.random, None)
            new_curr = new_curr.next
            curr = curr.next




        return new_head

        