# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        # Find sub-list from m to n
        count = 0
        reverse1 = None
        reverse2 = None
        t = head
        prev = ListNode('head')
        prev.next = head
        while t:
            if count == m - 1:
                reverse1 = t
                p1 = prev
            if count == n - 1:
                reverse2 = t
                break
            prev = t
            t = t.next
            count += 1

        # Reverse reverse1 to reverse2
        p2 = reverse2.next 
        reverse2.next = None

        # Reverse reverse1 to reverse2
        reverse3 = self.reverse(reverse1)

        p1.next = reverse3

        t = p1
        while t.next:
            t = t.next

        t.next = p2
        
        if p1.val == 'head':
            return p1.next
        return head
    
    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head 
            head = next
        return prev
    
    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next