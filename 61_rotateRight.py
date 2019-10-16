# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        count = 0
        le=self.findLength(head)
        re=k%le
        while count < re:
            head = self.rotateOnce(head)
            count = count +1
        return head
        
    def findLength(self,head):
        curr = head
        count = 1
        while curr.next != None:
            curr = curr.next
            count = count + 1 
        return count

    def rotateOnce(self, head):
        curr = head
        pointer = head.next
        while pointer.next != None:
            curr = curr.next
            pointer = pointer.next
            
        pointer.next = head
        curr.next = None
        return pointer
