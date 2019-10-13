class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target == None or len(str(target)) == 0:
            return False
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            if len(matrix[0]) == 0:
                return False
            r = 0
            return self.bs(matrix[r], target, 0, len(matrix[r])-1, (len(matrix[r])-1)/2)
        sidx = 0
        eidx = len(matrix)-1
        idx = len(matrix)/2
        ln = idx
        while sidx<eidx-1:
            if matrix[idx][0] == target :
                return True
            elif matrix[idx][0]>target:
                eidx = idx
            else:
                sidx = idx                
            idx = (sidx + eidx)/2
            ln = ln/2
        if matrix[sidx][0] == target or matrix[eidx][0] == target:
            return True
        r = sidx
        if target>matrix[eidx][0]:
            r = eidx
        return self.bs(matrix[r], target, 0, len(matrix[r])-1, (len(matrix[r])-1)/2)

                        
    def bs(self,row, target, sidx, eidx, idx):
        if row[idx] == target:
            return True
        if sidx==eidx-1 or sidx == eidx:
            if target in row[sidx:eidx+1]:
                return True
            else:
                return False
        
        if row[idx]>target:
            eidx = idx
        else:
            sidx = idx
        idx = (sidx+eidx)/2
        return self.bs(row, target, sidx, eidx, idx)
            
