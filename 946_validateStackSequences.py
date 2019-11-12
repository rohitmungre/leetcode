import copy
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        return self.vss(pushed, popped, 0, 0, [])
        
    def vss(self, pushed, popped, pu, po, st):
        if pu == len(pushed) and po == len(popped):
            return True
        if po == len(popped):
            return False
        
        if pu == 0:            
            st.insert(0, pushed[pu])
            pu = pu+1
        
        if len(st) == 0:
            st.insert(0, pushed[pu])
            pu = pu+1
            return self.vss(pushed, popped, pu, po, st) 
            
        if st[0] == popped[po]:
            po = po+1
            cst = copy.copy(st)
            cst.pop(0)
            res2 = self.vss(pushed, popped, pu, po, cst)            
            return res2
        else:
            if pu == len(pushed):
                return False
            st.insert(0, pushed[pu])
            pu = pu+1
            return self.vss(pushed, popped, pu, po, st)
