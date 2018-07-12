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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        left, right = l1, l2
        root, current = None, None

        def bind_next(node):
            nonlocal root
            nonlocal current

            if not root:
                root = current = node
            else:
                current.next = node
                current = node

        while left and right:
            if left.val < right.val:
                bind_next(left)
                left = left.next
            else:
                bind_next(right)
                right = right.next

        next_node = left and left or right
        if current:
            current.next = next_node
        else:
            return next_node

        return root


x = Solution()
ListNode.printof(x.mergeTwoLists(ListNode.generate_node([1, 2, 4]), ListNode.generate_node([1, 3, 4])))