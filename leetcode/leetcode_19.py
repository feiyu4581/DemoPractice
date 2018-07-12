# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def generate_node(cls, vals):
        root, current = None, None
        for val in vals:
            node = cls(val)
            if not root:
                root = node

            if current:
                current.next = node

            current = node

        return root

    @staticmethod
    def printof(head):
        current = head
        while current:
            print (current.val)
            current = current.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        index = 0
        current = head
        res = {}
        while current:
            res[index] = current
            current = current.next

            index += 1

        target = index - n
        if target == 0:
            return head.next
        elif target + 1 == index:
            res[target - 1].next = None
        elif target > 0:
            res[target - 1].next = res[target + 1]

        return head

x = Solution()
ListNode.printof(x.removeNthFromEnd(ListNode.generate_node([1, 2, 3, 4, 5]), 2))