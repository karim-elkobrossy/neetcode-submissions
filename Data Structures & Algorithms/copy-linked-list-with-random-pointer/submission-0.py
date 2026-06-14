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
        curr=head
        dummy_node=Node(0, None, None)
        new_head=dummy_node
        curr_new=new_head
        old_to_new = {}
        while curr:
            val = curr.val
            next_node = curr.next
            new_node = Node(val, next_node, None)
            old_to_new[curr] = new_node
            curr_new.next=new_node
            curr=curr.next
            curr_new=curr_new.next
        
        curr=head
        curr_new=new_head.next
        while curr:
            curr_new.random = old_to_new[curr.random] if curr.random else None
            curr=curr.next
            curr_new=curr_new.next
        return new_head.next