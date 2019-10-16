# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
                
        s, fts = self.ffts(root)
        from collections import Counter
        from itertools import groupby

        # group most_common output by frequency
        freqs = groupby(Counter(fts).most_common(), lambda x:x[1])
        # pick off the first group (highest frequency)
        return [val for val,count in next(freqs)[1]]
                
    def ffts(self, root):
        if root == None:
            return 0, []
        
        ls = 0
        lfts = []
        if root.left != None:
            ls, lfts = self.ffts(root.left)

        rs = 0
        rfts = []
        if root.right != None: 
            rs, rfts = self.ffts(root.right)
            
        s = ls + rs + root.val
        fts = lfts + [s] + rfts
        return s, fts
