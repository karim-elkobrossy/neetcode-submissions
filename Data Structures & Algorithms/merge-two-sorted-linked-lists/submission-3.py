# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Heads of lists
        l1, l2 = list1, list2
        # New list
        head_l3 = ListNode(None, None)
        curr_l3 = head_l3

        while l1 and l2:
            if l1.val < l2.val:
                curr_l3.next=l1
                curr_l3=l1
                l1=l1.next
            else:
                curr_l3.next=l2
                curr_l3=l2
                l2=l2.next            
        while l1:
            curr_l3.next=l1
            curr_l3=l1
            l1=l1.next
        while l2:
            curr_l3.next=l2
            curr_l3=l2
            l2=l2.next
        
        return head_l3.next



