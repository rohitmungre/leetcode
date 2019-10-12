class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        
        lo =0
        mid = 0
        hi = len(nums)-1
        flag = 0
        while(mid<= hi):
            if flag == 0:
                flag = 1
                if nums[lo] == 0:
                    flag = 0
                    lo = lo+1
                    mid = mid+1
                if nums[hi] == 2:
                    flag = 0
                    hi = hi-1
            else:
                if nums[mid] == 0:
                    if lo == mid:
                        lo=lo+1
                        mid=mid+1
                    else:    
                        tmp = nums[lo]
                        nums[lo] = nums[mid]
                        nums[mid] = tmp
                        lo = lo + 1
                elif nums[mid] == 2:
                    tmp = nums[hi]
                    nums[hi] = nums[mid]
                    nums[mid] = tmp
                    hi = hi -1
                if nums[mid] == 1:
                        mid = mid + 1
                    
        return nums
