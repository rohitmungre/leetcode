# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        
        aage = head
        peeche = head
        
        for i in range(n):
            aage = aage.next
            
        if aage == None:
            head = head.next 
            return head
            
        while aage.next != None:
            aage = aage.next 
            peeche = peeche.next 
            
        nikalo = peeche.next
        yaha_jodo = nikalo.next
        
        peeche.next = yaha_jodo
        
        return head
        
