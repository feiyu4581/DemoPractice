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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start, current = head, head.next
        while current:
            if current.val != start.val:
                start.next = current
                start = current
            else:
                start.next = None

            current = current.next

        return head


x = Solution()
ListNode.printof(x.deleteDuplicates(ListNode.generate_node([1, 1, 2])))

print('---')
ListNode.printof(x.deleteDuplicates(ListNode.generate_node([1, 2, 3, 3, 4, 4, 5, 5])))
print('---')

ListNode.printof(x.deleteDuplicates(ListNode.generate_node([1, 1, 2, 3, 3])))
        