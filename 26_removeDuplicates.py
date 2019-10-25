class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        slow = 0
        fast = 1
        
        while fast<len(nums):
            if nums[slow] == nums[fast]:
                fast = fast+1
            else:
                nums[slow+1] = nums[fast]
                slow = slow + 1 
                fast = fast + 1
        return slow+1 
