# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Retrieve the length of the linked list
        curr, len_ll = head, 0
        while curr:
            len_ll+=1
            curr=curr.next
        
        new_head, curr = ListNode(None, head), head
        prev = new_head
        nth_el = len_ll - n
        count = 0

        while curr:
            if count==nth_el:
                # delete this node
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            count+=1
            
        return new_head.next

