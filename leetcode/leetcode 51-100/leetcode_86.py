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

    def __repr__(self):
        vals = []
        current = self
        while current:
            vals.append(current.val)
            current = current.next

        return '<ListNode {}>'.format(vals)

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start, current, prev = dummy, head, dummy
        while current:
            if current.val < x:
                if start.next is current:
                    start, current, prev = current, current.next, current
                else:
                    current.next, start.next, prev.next = start.next, current, current.next
                    start, current, prev = start.next, prev.next, prev
            else:
                prev, current = current, current.next

        return dummy.next


x = Solution()
ListNode.printof(x.partition(ListNode.generate_node([1, 4, 3, 2, 5, 2]), 3))
        