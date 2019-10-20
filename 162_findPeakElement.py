class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<=1:
            return 0
        return self.fpe(nums, 0, len(nums)-1)
        
    def fpe(self, nums, sidx, eidx):
        print(nums, sidx,eidx)
        if sidx == eidx:
            return sidx
        
        if sidx == eidx-1:
            if nums[sidx]>nums[eidx]:
                if sidx == 0:
                    return sidx
                elif nums[sidx]>nums[sidx-1]:
                    return sidx
                else:
                    print('wrong test case1')

            elif nums[eidx]>nums[sidx] :
                if eidx == len(nums)-1:
                    return eidx
                elif nums[eidx]>nums[eidx+1]:
                    return eidx
                else:                    
                    print('wrong test case2')

            else:
                'wrong test case3'
        midx = (sidx+eidx)/2
        if nums[midx]>nums[midx+1]:
            if nums[midx]>nums[midx-1]:
                return midx
            return self.fpe(nums, sidx, midx-1)
        return self.fpe(nums, midx+1,eidx)
