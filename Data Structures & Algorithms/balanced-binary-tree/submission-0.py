# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height_diff(self, root):
        if root == None: return 0
        left_h = self.height_diff(root.left)
        right_h = self.height_diff(root.right)
        diff = abs(left_h-right_h)
        if diff > 1: self.isbalanced = False
        print(left_h, right_h, max(left_h, right_h)+1)
        return max(left_h, right_h)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced=True
        self.height_diff(root)
        return self.isbalanced