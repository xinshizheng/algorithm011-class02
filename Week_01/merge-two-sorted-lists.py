class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = res = ListNode(None)
        while True:
            try:
                while l1.val <= l2.val:
                    p.next = l1
                    l1, p = l1.next, p.next
                while l1.val > l2.val:
                    p.next = l2
                    l2, p = l2.next, p.next
            except: 
                break
        p.next = l1 or l2
        return res.next