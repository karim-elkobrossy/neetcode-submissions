# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [[root, 0]]
        levelOrder_lst = [[root.val]]
        while queue:
            curr_node, level = queue.pop(0)
            left_child = curr_node.left
            right_child = curr_node.right
            if left_child: 
                queue.append([left_child, level+1]) 
                print(level+1, levelOrder_lst)
                try: levelOrder_lst[level+1].append(left_child.val)
                except: levelOrder_lst.append([left_child.val])
            if right_child: 
                queue.append([right_child, level+1])
                try: levelOrder_lst[level+1].append(right_child.val)
                except: levelOrder_lst.append([right_child.val])
        return levelOrder_lst