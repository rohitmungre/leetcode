import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<1:
            return[nums]
        
        return self.subsets(nums,[])
        
    def subsets(self, nums, memo):
        if len(nums) == 1:
            el = nums.pop()
            memo.append(str(el))
            return [[el], []]
        
        el = nums.pop()
        s = self.subsets(nums,memo)
        cs = copy.deepcopy(s)
        indexes = []
        for i in range(0,len(cs)):
            cs[i] = cs[i]+ [el]
            cs[i].sort()
            
        for i in range(0, len(cs)):
            mstr = '~'.join([str(iii) for iii in cs[i]])
            if mstr in memo:
                indexes.append(i)
            else:
                memo.append(mstr)

        for index in sorted(indexes, reverse=True):
            del cs[index] 
        
        return s+cs
        
        
