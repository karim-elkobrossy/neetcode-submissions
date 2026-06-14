# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        curr=head
        # If linked list is empty
        if curr==None: return
        nodes.append(head)
        while curr.next!=None:
            nodes.append(curr.next)
            curr=curr.next
        
        # Take the last node from the list and point next to the previous node
        curr_node = nodes.pop()
        head=curr_node
        while len(nodes)>0:
            prev_node = nodes.pop()
            curr_node.next=prev_node
            curr_node=prev_node
        curr_node.next=None

        return head
            

