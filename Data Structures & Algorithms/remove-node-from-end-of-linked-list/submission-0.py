# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        curr=head
        count=0
        del_pos = length-n
        print(del_pos)
        if del_pos<0: return
        while True:
            # Deleting first element
            if del_pos == 0:
                head = head.next
                break
            if count==(del_pos-1):
                print(count)
                deleted = curr.next
                curr.next = curr.next.next
                deleted=None
                break
            curr=curr.next
            count+=1
        return head