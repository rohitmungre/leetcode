class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
            
        #flip 
        for i in range(len(A)):
            for j in range(len(A[0])/2):
                tmp = A[i][j]
                A[i][j] = A[i][-1*j -1]
                A[i][-1*j -1] = tmp
            
        #invert
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
                    
        return A
