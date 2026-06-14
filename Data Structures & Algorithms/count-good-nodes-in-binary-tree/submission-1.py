# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        We use BFS algorithm to propagate the maximum element downwards for each branch.
        """
        if not root: return []
        queue = [(root, root.val)]
        count=0
        while queue:
            curr_node, max_branch = queue.pop(0)
            if curr_node.val>=max_branch: count+=1
            left = curr_node.left
            right = curr_node.right
            if left: queue.append((left, max(max_branch, left.val)))
            if right: queue.append((right, max(max_branch, right.val)))
        return count 