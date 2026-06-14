# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            # Traverse left subtree, root, and then right subtree
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Perform an in-order traversal and return the k-1th element (1-indexed)
        return inorder(root)[k-1]