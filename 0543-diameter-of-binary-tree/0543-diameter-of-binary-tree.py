# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def rec(curr):

            if not curr:
                return 0
            
            left = rec(curr.left)
            right  = rec(curr.right)
            self.res =  max(self.res , left+right)

            return 1 + max( left,right)

        rec(root)
        return self.res
        