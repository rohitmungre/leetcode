# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1 
        if root.left != None:
            h1 = self.minDepth(root.left)  
        else:
            return 1+self.minDepth(root.right)
        if root.right != None:
            h2 = self.minDepth(root.right)
            return 1 + min(h1,h2)
        else:
            return 1+h1
