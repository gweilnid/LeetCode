# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        result = []
        current_l1 = l1
        current_l2 = l2
        add_on = False
        idx = 0
        while current_l1 is not None or current_l2 is not None:
            x = current_l1.val if current_l1 else 0
            y = current_l2.val if current_l2 else 0
            result.append(x+y)
            current_l1 = current_l1.next if current_l1 else None
            current_l2 = current_l2.next if current_l2 else None
            if add_on:
                result[idx] += 1
                add_on = False
            if result[idx] > 9:
                add_on = True
                result[idx] -= 10
            cur.next = ListNode(result[idx])
            cur = cur.next
            idx += 1
        if add_on:
            cur.next = ListNode(1)
        return dummy.next