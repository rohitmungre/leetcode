class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n <=0:
            return []
        if n == 1:
            return matrix[0]
        
        m = len(matrix[0])
        cnt = 0
        ir=0
        ic=0
        layer = 0
        dir = 'right'
        res = []
        while cnt<m*n:
            cnt = cnt+1
            res.append(matrix[ir][ic])
            
            if dir == 'right':
                if ic == len(matrix[0])-layer-1:
                    dir = 'down'
                    ir = ir+1
                else:
                    ic = ic +1
            elif dir == 'down':
                if ir == len(matrix) - layer -1:
                    dir = 'left'
                    ic =ic-1
                else:
                    ir = ir+1
            elif dir == 'left':
                if ic == layer:
                    dir = 'up'
                    ir=ir-1
                else:
                    ic = ic -1
            elif dir == 'up':
                if ir == layer + 1:
                    dir = 'right'
                    layer = layer + 1
                    ic = ic+1
                else:
                    ir = ir-1
        return res
