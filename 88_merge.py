class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2)==0 or len(nums1)==0:
            return
        p1=0
        p2=0
        tmp=[]
        while p1<m+n:
            if p2 >= n:
                if p1>=m:
                    nums1[p1] = tmp.pop(0)
                elif len(tmp) == 0:
                    return
                else:
                    tmp.append(nums1[p1])
                    nums1[p1] = tmp.pop(0)
            else:                
                if p1 >= m:
                    if len(tmp) == 0:
                        nums1[p1] = nums2[p2]
                        p2 = p2 + 1
                    elif tmp[0] < nums2[p2]:
                        nums1[p1] = tmp.pop(0)
                    else:
                        nums1[p1] = nums2[p2]
                        p2 = p2 + 1
                else:        
                    if len(tmp) == 0:
                        if nums1[p1]>nums2[p2]:
                            tmp.append(nums1[p1])
                            nums1[p1] = nums2[p2]
                            p2 = p2 + 1
                    else:
                        if tmp[0] < nums1[p1] and tmp[0] <= nums2[p2]:
                            tmp.append(nums1[p1])
                            nums1[p1] = tmp.pop(0)                        
                        elif nums2[p2] <= tmp[0] and nums2[p2]<nums1[p1]:
                            tmp.append(nums1[p1])
                            nums1[p1] = nums2[p2]
                            p2 = p2+1
            p1 = p1+1                    
