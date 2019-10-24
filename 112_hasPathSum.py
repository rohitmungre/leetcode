# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """        
        if root == None:
            return False
        
        if root.val == sum and root.left == None and root.right == None:
            return True

        r1 = False
        r2 = False
        if root.left != None:
            r1 = self.hasPathSum(root.left, sum - root.val)
                                 
        if root.right != None:
            r2 = self.hasPathSum(root.right, sum - root.val)
        
        return (r1 or r2)
