# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return 0 
        lsm = self.rangeSumBST(root.left, L, R)
        rsm = self.rangeSumBST(root.right, L, R)

        if root.val >= L and root.val <= R:
            sm = root.val
        else:
            sm = 0     
        return sm + lsm + rsm
