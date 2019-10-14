# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        if head.next == None:
            return False
        slow = head.next 
        fast = slow.next
        
        while fast and slow:
            if slow == fast :
                return True
            slow = slow.next 
            fast = fast.next 
            if fast == None:
                return False
            fast = fast.next
            
        return False
