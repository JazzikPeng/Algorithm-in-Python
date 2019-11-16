# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
    
        prev = ListNode(None)
        prev.next = head
        re = prev
        while head:
            # print(head.val, prev.val)
            if head.val == val:
                prev.next = head.next
                # print(head.val)
            else:
                prev = head
            head = head.next
        return re.next