# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def append(self, val):
            new_node = ListNode(val)
            if self.end is not None:
                self.end.next = new_node
            else: self.head=new_node
            self.end = new_node

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = None
        i, j = list1, list2
        self.head=self.end=None
        while i is not None and j is not None:
            if i.val<=j.val:
                self.append(i.val)
                i=i.next
            else: 
                self.append(j.val)
                j=j.next   
        while i is not None:
            self.append(i.val)
            i=i.next
        while j is not None:
            self.append(j.val)
            j=j.next
        return self.head