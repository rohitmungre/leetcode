# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        curr = head
        nxt = head.next
        
        while nxt != None:            
            if nxt.val == curr.val:
                curr.next = nxt.next
                nxt = nxt.next
            else:
                curr = nxt
                nxt = nxt.next            
            
        return head
