import copy
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = copy.copy(A)
        B.sort()
        k_arr = []
        for i in range(len(A)-1,-1,-1):
            if A[i] != B[i]:
                idx = A.index(B[i])
                A = self.pancakeFlip(A, idx)
                A = self.pancakeFlip(A, i)
                k_arr.append(idx+1)
                k_arr.append(i+1)
        return k_arr 
            
    def pancakeFlip(self, A, k):
        temp = range(k+1)
        for i in range(k+1):
            temp[i] = A[k-i]
        A[0:k+1] = temp
        return A
        
