# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return None
        slow = head.next 
        fast = slow.next
        sc = 1
        fc = 2
        while fast and slow:
            if slow == fast :
                tracker = head
                while slow != tracker:
                    slow = slow.next
                    tracker = tracker.next
                return slow
            slow = slow.next 
            sc = sc+1
            fast = fast.next 
            fc = fc+1
            if fast == None:
                return None
            fast = fast.next
            fc = fc+1
            
        return None
