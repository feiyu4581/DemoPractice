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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        current, start, prev, start_prev = head, head, None, None
        index = 1
        while current:
            if index == m:
                start_prev, start = prev, current
            elif m < index <= n:
                current.next, current, prev = prev, current.next, current
                if index == n:
                    start.next = current
                    if start_prev:
                        start_prev.next = prev
                    else:
                        head = prev

            if index <= m or index > n:
                prev = current
                current = current.next

            index += 1

        return head

    
x = Solution()
# ListNode.printof(x.reverseBetween(ListNode.generate_node([1, 2, 3, 4, 5]), 2, 4))
ListNode.printof(x.reverseBetween(ListNode.generate_node([3, 5]), 1, 2))
        