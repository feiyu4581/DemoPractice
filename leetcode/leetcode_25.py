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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        index = 1
        prev = dummy
        while head:
            if head.next:
                if index + 1 == k:
                    next_next_node = head.next.next
                    start, end = self.exchange_node(prev.next, head.next)
                    prev.next, end.next = start, next_next_node
                    prev, head, index = end, next_next_node, 1
                else:
                    head = head.next
                    index += 1
            else:
                head = None

        return dummy.next

    def exchange_node(self, start, end):
        prev, current = start, start.next
        while current != end:
            next_node = current.next

            current.next = prev
            prev = current
            current = next_node

        end.next = prev
        return end, start
        

x = Solution()
ListNode.printof(x.reverseKGroup(ListNode.generate_node([1, 2, 3, 4, 5]), 2))
ListNode.printof(x.reverseKGroup(ListNode.generate_node([1, 2, 3, 4, 5]), 3))
