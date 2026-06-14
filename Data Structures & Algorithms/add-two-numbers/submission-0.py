# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0, None)
        curr=head
        carry,rem=0,0
        while (l1 and l2):
            addition = l1.val+l2.val+carry
            carry, rem = int(addition/10), addition%10
            curr.next = ListNode(rem, None)
            curr=curr.next
            l1=l1.next
            l2=l2.next
        while l1:
            addition = l1.val+carry
            carry, rem = int(addition/10), addition%10
            curr.next = ListNode(rem, None)
            curr=curr.next
            l1=l1.next
        while l2:
            addition = l2.val+carry
            carry, rem = int(addition/10), addition%10
            curr.next = ListNode(rem, None)
            curr=curr.next
            l2=l2.next
        if carry: curr.next = ListNode(1, None)
        return head.next
        
        return head.next


        
        




        