# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        identical = True
        p_queue, q_queue, elements = [], [], []
        p_queue.append(p)
        while p_queue:
            el = p_queue.pop(0)
            # Add value of current and 2 children
            if el is None: 
                elements.append(None)
                continue
            elements.append(el.val)
            if not el.left and not el.right: continue
            p_queue.append(el.left)
            p_queue.append(el.right)
        print(elements)

        q_queue.append(q)
        while q_queue:
            # If the elements in the first tree finished, then they are not identical
            if not elements:
                identical = False
                return identical
            el = q_queue.pop(0)
            if not el:
                if elements.pop(0)!=None:
                    identical = False
                    return identical
                else: continue 
            if el.val!=elements.pop(0): 
                identical = False
                return identical
            if not el.left and not el.right: continue
            q_queue.append(el.left)
            q_queue.append(el.right)
        
        # If the loop finished and there are values left from p, then elements (list) would still have some elements
        if elements: return False
        return identical

#Leetcode
"""def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False"""