class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <=0:
            return []
        if n == 1:
            return [[1]]
        mat = [[0 for i in range(0,n)] for j in range(0,n)]
        
        cnt = 0
        ir=0
        ic=0
        layer = 0
        dir = 'right'
        while cnt<n*n:
            cnt = cnt+1
            mat[ir][ic] = cnt
            
            if dir == 'right':
                if ic == len(mat)-layer-1:
                    dir = 'down'
                    ir = ir+1
                else:
                    ic = ic +1
            elif dir == 'down':
                if ir == len(mat) - layer -1:
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
        return mat
