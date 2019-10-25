class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        y = 0
        x = 0
        
        for item in moves: 
            if item == 'U':
                y = y +1
            elif item == 'D':
                y = y -1
            elif item == 'L':
                x = x -1
            elif item == 'R':
                x = x +1
            
        if x==0 and y==0:
            return True
        
        return False
