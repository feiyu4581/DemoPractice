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

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        current, last, before, root = head, None, None, head.next
        while current:
            if last:
                last.next = current.next
                current.next = last
                if before:
                    before.next = current

                before = last
                current = last.next
                last = None
            else:
                last = current
                current = current.next

        return root

    def swapPairs2(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.next:
                pre.next = head.next
                head.next.next, head.next = head, head.next.next
                pre, head = head, head.next
            else:
                head = None

        return dummy.next
        

x = Solution()
ListNode.printof(x.swapPairs2(ListNode.generate_node([1, 2, 3, 4, 5])))
ListNode.printof(x.swapPairs2(ListNode.generate_node([2, 5, 3, 4, 6, 2, 2])))
ListNode.printof(x.swapPairs2(ListNode.generate_node([1])))
ListNode.printof(x.swapPairs2(ListNode.generate_node([])))