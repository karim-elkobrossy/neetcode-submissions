# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative solution
        """nodes=[]
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

        return head"""

        # Recursive solution
        def Recursive(head, node):
            if node.next==None: return (node, node)
            (head, after_node) = Recursive(head, node.next)
            after_node.next=node
            return (head, node)
        
        if head==None: return
        node=head
        new_head, node = Recursive(head, node)
        node.next=None
        # Setting first original next pointer node to Null
        return new_head
            

