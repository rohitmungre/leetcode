class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        cnt=0
        charmap = self.createMap(chars)
        for item in words:
            wordmap = self.createMap(item)
            if self.findSubMap(wordmap,charmap):                            
                cnt = cnt + len(item)            
        return cnt
    
    def createMap(self,st):
        map = {}
        for char in list(st):
            if char in map:
                map[char] = map[char]+1
            else:
                map[char] = 1                
        return map
        
    def findSubMap(self, wm, cm):        
        for item in wm:
            if item not in cm:
                return False
            if wm[item]>cm[item]:
                return False
        return True
