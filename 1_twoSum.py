class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<2:
            return []
        
        memo={}
        for i in range(0, len(nums)):
            if (target - nums[i]) in memo:
                return[memo[target-nums[i]], i]
            memo[nums[i]] = i
        return []                
