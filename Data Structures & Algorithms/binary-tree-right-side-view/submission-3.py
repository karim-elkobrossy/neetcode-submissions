# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = [root]
        visible_elements = [root.val]
        while queue:
            num_elements = len(queue)
            for i in range(num_elements):
                curr = queue.pop(0)
                left_child = curr.left
                right_child = curr.right
                if left_child: queue.append(left_child)
                if right_child: queue.append(right_child)
            # Collect elements on the same tree level
            # Take the last element in a level array to be the visible element in that level
            if queue: visible_elements.append(queue[-1].val)
        return visible_elements


        