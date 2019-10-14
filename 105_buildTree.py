# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if len(preorder) == 0:
            return None
        
        roo = preorder[0]
        idx = inorder.index(roo)
        
        left_in = inorder[:idx]
        right_in = inorder[idx+1:]
        
        left_pre = preorder[1:idx+1]
        right_pre = preorder[idx+1:]
        
        root = TreeNode(roo)
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        
        return root
        
