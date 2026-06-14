# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            # The current node's value must be between low and high
            if not (low < node.val < high):
                return False
            # Recursively check the subtrees with updated ranges
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        # Initially, the range is infinite
        return dfs(root, float('-inf'), float('inf'))