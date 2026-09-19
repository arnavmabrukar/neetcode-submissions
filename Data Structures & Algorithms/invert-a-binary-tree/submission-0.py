# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # no tree? do nothing
        if not root:
            return None
        
        # tree? then swap
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # call the function recursively
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root