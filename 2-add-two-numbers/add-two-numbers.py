# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        l1_ptr = l1
        l2_ptr = l2
        add_on = False
        idx = 0
        while l1_ptr is not None or l2_ptr is not None:
            x = l1_ptr.val if l1_ptr else 0
            y = l2_ptr.val if l2_ptr else 0
            val = x+y
            l1_ptr = l1_ptr.next if l1_ptr else None
            l2_ptr = l2_ptr.next if l2_ptr else None
            if add_on:
                val += 1
                add_on = False
            if val > 9:
                add_on = True
                val %= 10
            res.next = ListNode(val)
            res = res.next
            idx += 1
        if add_on:
            res.next = ListNode(1)
        return dummy.next