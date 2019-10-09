import copy

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return strs
        if len(strs) == 1:
            return [strs]
        def_dic = {'a':0, 'b':0, 'c':0, 'd':0,'e':0, 'f':0, 'g':0, 'h':0,'i':0, 'j':0,'k':0,'l':0,'m':0,'n':0, 'o':0, 'p':0,'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,'y':0,'z':0}
        
        res = {}
        for item in strs:
            smap = self.find_mapping(item, def_dic)
            
            if smap in res:
                res[smap] = res[smap] + [item]
            else:
                res[smap] = [item]
        
        lis = []
        for keys in res:
            lis.append(res[keys])
            
        return lis
        
    def find_mapping(self, st, def_dic):
        dic = copy.copy(def_dic)
        for i in list(st):
            dic[i] = dic[i]+1
        st = self.convert_into_str(dic)
        return st

    def convert_into_str(self, dic):
        st = ''
        for i in dic:
            st = st + '~' + str(dic[i])
        return st
