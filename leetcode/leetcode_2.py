
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, left, right):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        res = None
        first = None
        while left or right:
            num = (left and left.val or 0) + (right and right.val or 0) + carry
            if num >= 10:
                num -= 10
                carry = 1
            else:
                carry = 0

            node = ListNode(num)
            if res:
                res.next = node
            else:
                first = node

            res = node

            left = left and left.next or None
            right = right and right.next or None

        if carry:
            res.next = ListNode(1)

        return first

        
x = Solution()

left = ListNode(2)
left.next = ListNode(4)
left.next.next = ListNode(3)

right = ListNode(5)
right.next = ListNode(6)
right.next.next = ListNode(4)
res = x.addTwoNumbers(left, right)

while res:
    print res.val
    res = res.next

left = ListNode(1)
left.next = ListNode(8)

right = ListNode(0)
res = x.addTwoNumbers(left, right)

while res:
    print res.val
    res = res.next