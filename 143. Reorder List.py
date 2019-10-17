# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This problem have two parts
# 1. Find the mid point - fast ad slow pointer
# 2. Reverse list
# 3. Reconstruct list
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        mid = self.findMid(head) # return the mid node
        #self.print_list(mid)
        # self.print_list(head)
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        l1 = head
        # self.print_list(head)
        # self.print_list(head)
        while  l1 is not None and l2 is not None:
            next =  l1.next
            l1.next = l2
            l2 = l2.next # Update l2 first otherwise, l1.next is still l2, l1.next.next will modify l2.next as well.
            l1.next.next = next 
            l1 = next

    def findMid(self, head):
        # Find mid note in a list
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    # Reverse linklist
    def reverse(self, head):
        newHead = None
        while head:
            next = head.next
            head.next = newHead
            newHead = head
            head = next
        return newHead

    def print_list(self, head):
        s = ''
        while head:
            s += str(head.val) + ' '
            head = head.next
        print(s)