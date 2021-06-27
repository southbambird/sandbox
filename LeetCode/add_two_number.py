# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        carry = 0
        for (n1, n2) in zip(l1, l2):
            sum = n1 + n2
            result.val = (sum + carry) % 10
            if (sum > 9):
                carry = 1
            else:
                carry = 0
