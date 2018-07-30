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
        dummy = ListNode(0)
        start, prev, repeat_num = dummy, None, 1
        while head:
            if prev is None:
                prev = head
            elif head.val == prev.val:
                repeat_num += 1
            else:
                if repeat_num == 1:
                    start.next, start = prev, prev
                    # start = prev
                    start.next = None
                else:
                    repeat_num = 1

                prev = head
            
            head = head.next

        if prev and repeat_num == 1:
            start.next = prev

        return dummy.next


x = Solution()
ListNode.printof(x.deleteDuplicates(ListNode.generate_node([1, 2, 3, 3, 4, 4, 5])))

print('---')
ListNode.printof(x.deleteDuplicates(ListNode.generate_node([1, 2, 3, 3, 4, 4, 5, 5])))
print('---')

ListNode.printof(x.deleteDuplicates(ListNode.generate_node([1, 1, 1, 2, 3])))
        