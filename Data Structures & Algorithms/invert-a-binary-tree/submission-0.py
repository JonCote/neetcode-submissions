# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recHelper(root)

        return root
        

    def recHelper(self, curr: Optional[TreeNode]):

        if curr == None:
            return

        if curr.left == None and curr.right == None:
            return

        l = curr.left
        curr.left = curr.right
        curr.right = l

        if curr.left != None:
            self.recHelper(curr.left)
        
        if curr.right != None:
            self.recHelper(curr.right)
        