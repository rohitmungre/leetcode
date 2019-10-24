class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sidx = 0
        eidx = len(nums)-1
        if len(nums) == 0:
            return 0
        while nums[eidx] == val:
            if eidx == 0:
                return 0
            eidx = eidx-1
        for sidx, item in enumerate(nums):
            if sidx == eidx:
                return sidx+1
            if sidx > eidx:
                return sidx
            if item == val:
                nums[sidx] = nums[eidx]
                nums[eidx] = val
                eidx = eidx-1
                while nums[eidx] == val:
                    if eidx == sidx:
                        return sidx
                    eidx = eidx-1
        return sidx+1
