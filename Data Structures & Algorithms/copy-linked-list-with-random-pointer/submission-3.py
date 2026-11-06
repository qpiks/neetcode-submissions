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



        pointers = collections.defaultdict(lambda: Node(0))
        pointers[None] = None
        curr = head
        while curr:
            pointers[curr].val = curr.val
            pointers[curr].random = pointers[curr.random]
            pointers[curr].next = pointers[curr.next]
            curr = curr.next
        


        # pointers = {}
        # curr = head
        # while curr:
        #     pointers[curr] = Node(curr.val)
        #     curr = curr.next

        # curr = head
        # while curr:
        #     new_curr = pointers[curr]
        #     new_curr.next = pointers.get(curr.next, None)
        #     new_curr.random = pointers.get(curr.random, None)
        #     curr = curr.next




        return pointers[head]

        