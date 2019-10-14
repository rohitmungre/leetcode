# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        
        roo = postorder[-1]
        idx = inorder.index(roo)
        
        left_in = inorder[:idx]
        right_in = inorder[idx+1:]
        
        left_post = postorder[:idx]
        right_post = postorder[idx:-1]
        
        root = TreeNode(roo)
        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        
        return root
        
