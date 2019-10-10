# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        if root == None:
            return lis
        lis = self.iot(root,lis)
        return lis
        
    def iot(self, root, lis):
        if root == None:
            return lis
        if root.left != None:
            lis = self.iot(root.left,lis)        
        lis.append(root.val)
        if root.right != None:
            lis = self.iot(root.right,lis)
        return lis
        
