# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        if root == None:
            return lis
        lis = self.pot(root,lis)
        return lis
    
    def pot(self, root, lis):
        if root == None:
            return lis
        if root.left != None:
            lis = self.pot(root.left,lis)
        if root.right != None:
            lis = self.pot(root.right,lis)
        lis.append(root.val)
        return lis
        
