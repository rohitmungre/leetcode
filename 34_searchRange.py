class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        sidx = 0 
        eidx = len(nums)-1
        flag = 0
        start = -1
        while sidx<=eidx:
            if nums[(sidx+eidx)/2]==target:
                flag = 1
                eidx = (sidx+eidx)/2-1
            elif nums[(sidx+eidx)/2]>target:
                eidx = (sidx+eidx)/2-1
            elif nums[(sidx+eidx)/2]<target:
                if sidx == len(nums)-1:
                    break
                if nums[(sidx+eidx)/2+1]==target:
                    start = (sidx+eidx)/2+1
                    flag = 1
                    break
                if nums[(sidx+eidx)/2+1]>target:
                    return [-1,-1]
                sidx = (sidx+eidx)/2+1
        
        if flag ==0:
            return [-1,-1]
        start = (sidx+eidx)/2+1
        
        sidx = 0 
        eidx = len(nums)-1
        flag = 0
        while sidx<=eidx:
            if nums[(sidx+eidx)/2]==target:
                flag = 1
                sidx = (sidx+eidx)/2+1
            elif nums[(sidx+eidx)/2]<target:
                sidx = (sidx+eidx)/2+1
            elif nums[(sidx+eidx)/2]>target:
                if nums[(sidx+eidx)/2-1]==target:
                    end = (sidx+eidx)/2-1
                    return [start, end]
                if nums[(sidx+eidx)/2-1]<target:
                    break
                eidx = (sidx+eidx)/2-1

        end = eidx        
        return [start,end]
            
