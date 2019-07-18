# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp_head = prev = ListNode(None)
        prev.next = head
        cur = head
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return temp_head.next

head = ListNode(1)  
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
print(head)

s = Solution()
print(s.deleteDuplicates(head).val)