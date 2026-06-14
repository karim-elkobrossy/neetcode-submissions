# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Make a dummy node linking to head
        prev, curr = None, head

        while curr:
            # Preserving the next node
            next = curr.next
            # Reversing current node
            curr.next = prev
            prev = curr
            curr = next
        # prev now is the head of the new reversed list    
        return prev