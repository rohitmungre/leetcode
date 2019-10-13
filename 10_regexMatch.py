import copy

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.regex_matching(s, p, 0, 0, {})

    def regex_matching(self, st, rex, sidx, ridx, memo):
        mstr = str(sidx)+ '~' + str(ridx)
        if mstr in memo:
            return memo[mstr]
        
        if sidx >= len(st) and ridx >= len(rex):
            memo[mstr] = True
            return True

        if ridx >= len(rex):
            memo[mstr] = False
            return False

        if sidx >= len(st):
            if ridx == len(rex) -1:
                memo[mstr] = False
                return False
            if rex[ridx+1] == '*':
                memo[mstr] = self.regex_matching(st,rex,sidx,ridx+2,memo)
                return memo[mstr]
            memo[mstr] = False
            return False
        
        if ridx<len(rex)-1:
            if rex[ridx+1] == '*':
                if st[sidx] == rex[ridx]:
                    if sidx == len(st) - 1 and ridx == len(rex) -2: 
                        memo[mstr] = True
                        return True
                    memo[mstr] = self.regex_matching(st,rex,sidx,ridx+2,memo) or self.regex_matching(st,rex, sidx+1, ridx,memo)
                    return memo[mstr]
                elif rex[ridx] == '.':
                    if sidx == len(st) - 1 and ridx == len(rex) -2: 
                        memo[str] = True
                        return True
                    memo[mstr] = self.regex_matching(st,rex,sidx,ridx+2,memo) or self.regex_matching(st,rex,sidx+1,ridx,memo)
                    return memo[mstr]
                else:
                    memo[mstr] = self.regex_matching(st,rex,sidx,ridx+2,memo)
                    return memo[mstr]

        if rex[ridx] == '.' or rex[ridx] == st[sidx]:
            memo[mstr] = self.regex_matching(st,rex,sidx+1,ridx+1,memo)
            return memo[mstr]

        memo[mstr] = False
        return False
