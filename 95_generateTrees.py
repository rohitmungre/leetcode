# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """        
        if n <1:
            return []
        if n == 1:
            return [TreeNode(1)]
        return self.gt_dp(1,n, {})
    
    def gt_dp(self,n1, n2,memo):
        mstr = str(n1)+'~'+str(n2)
        if mstr in memo:
            return memo[mstr]
        if n1>n2:
            memo[mstr]=None
            return None
        if n1 == n2:
            memo[mstr]=[TreeNode(n1)]
            return [TreeNode(n1)]
        num = []
        for i in range(n1, n2+1):
            l = self.gt_dp(n1, i-1, memo)
            r = self.gt_dp(i+1, n2, memo)
            if l == None and r == None:
                head = TreeNode(i)
                num.append(head)
            elif l == None:
                for rr in r:
                    head = TreeNode(i)
                    head.right = rr                    
                    num.append(head)                
            elif r == None:
                for ll in l:
                    head = TreeNode(i)
                    head.left = ll
                    num.append(head)
            else:            
                for ll in l:
                    for rr in r:
                        head = TreeNode(i)
                        head.left = ll
                        head.right = rr                    
                        num.append(head)
        memo[mstr] = num
        return num

