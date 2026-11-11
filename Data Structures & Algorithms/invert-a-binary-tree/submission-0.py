# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        if root.left: 
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root

        # if self.left and self.right:
        #     self.left, self.right = self.right, self.left
        #     invertTree(self, self.left)
        #     invertTree(self, self.right)
        # elif self.left: 
        #     self.right = self.left
        #     invertTree(self, self.right)
        # if self.right:
        #     self.left = self.right
        #     self.right =
        #     invertTree(self, self.left)
                