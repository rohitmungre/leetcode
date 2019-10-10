# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val
        lis = []
        lis = self.ks(root, lis)
        return lis[k-1]
        
        
    def ks(self, root, lis):
        if root == None:
            return lis
        if root.left != None:
            lis = self.ks(root.left, lis)
        lis.append(root.val)
        if root.right != None:
            lis = self.ks(root.right, lis)
        return lis
