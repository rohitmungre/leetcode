class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """        
        if len(deck)==0:
            return deck
        deck.sort()        
        sdeck = [0 for i in range(len(deck))]
        
        pointer = 0
        sdeck[pointer] = deck[pointer]
        deck.pop(0)
        pointer = pointer+1
        while len(deck) > 0:
            pointer = self.ekelementhataak(deck,sdeck, pointer)    
        return sdeck
        
    def ekelementhataak(self, deck, sdeck, pointer):   
        while sdeck[pointer] != 0:
            pointer = pointer+1        
            if pointer >= len(sdeck):
                pointer = 0            
        skip_pointer = pointer 
        pointer = pointer+1
        if pointer >= len(sdeck):
            pointer = 0            
        while sdeck[pointer] != 0:
            pointer = pointer+1        
            if pointer >= len(sdeck):
                pointer = 0            
        sdeck[pointer] = deck[0]
        deck.pop(0)                
        return pointer
