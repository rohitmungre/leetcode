class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        if len(nums) <3:
            return min(nums)
        farr = []
        sarr = []
        for i in nums:
            if i in farr and i in sarr:
                continue
            elif i in farr:
                sarr.append(i)
            else:
                farr.append(i)
        
        return sum(farr) - sum(sarr)
        
