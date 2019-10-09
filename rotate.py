class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
    
        for i in range(0,len(matrix)):
            for j in range(i+1, len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        for i in range(0,len(matrix)):
            for j in range(0, len(matrix)/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix)-j-1]
                matrix[i][len(matrix)-j-1] = tmp

