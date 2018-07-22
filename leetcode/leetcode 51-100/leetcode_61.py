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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        heads, current = [], head
        while current:
            heads.append(current)
            current = current.next

        k %= len(heads)
        if k:
            heads[len(heads) - k - 1].next = None
            heads[-1].next = heads[0]
            return heads[len(heads) - k]

        return head


x = Solution()
ListNode.printof(x.rotateRight(ListNode.generate_node([1, 2, 3, 4, 5]), 2))
ListNode.printof(x.rotateRight(ListNode.generate_node([0, 1, 2]), 4))
