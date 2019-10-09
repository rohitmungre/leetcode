import copy

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        if len(nums)<=1:
            return [nums]
        res = []
        unique_nums = []
        for i in range(0, len(nums)):
            cnums = copy.copy(nums)
            el = cnums.pop(i)
            if el not in unique_nums:                
                unique_nums.append(el)
                m_el = self.permuteUnique(cnums)
                for j in range(0, len(m_el)):
                    tmp =[el]+m_el[j]
                    m_el[j]=tmp
                res=res+m_el
        return res
