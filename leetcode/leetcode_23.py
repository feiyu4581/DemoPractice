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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        while len(lists) >= 2:
            lists.append(self.mergeTwoLists(lists.pop(), lists.pop()))

        return lists[0]

    def mergeTwoLists(self, l1, l2):
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

    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        lists = [node for node in lists if node]
        if not lists:
            return []

        root, current = None, None
        while len(lists) >= 2:
            min_value, min_node, min_index = float('inf'), None, -1
            for index, node in enumerate(lists):
                if node.val < min_value:
                    min_value, min_node, min_index = node.val, node, index

            if not root:
                root = current = min_node
            else:
                current.next = min_node
                current = current.next

            if not min_node.next:
                lists.remove(min_node)
            else:
                lists[min_index] = min_node.next

        if not root:
            return lists[0]
        else:
            current.next = lists[0]

        return root


    def mergeKLists3(self, lists):
        if not lists:
            return None

        node_vals = {}
        for node in lists:
            if not node:
                continue

            while node:
                node_vals.setdefault(node.val, 0)
                node_vals[node.val] += 1

                node = node.next

        keys = node_vals.keys()
        root = current = ListNode(None)
        for key in sorted(keys):
            for _ in range(node_vals[key]):
                current.next = ListNode(key)
                current = current.next

        return root.next

x = Solution()
ListNode.printof(x.mergeKLists3([
    ListNode.generate_node([1, 4, 5]),
    ListNode.generate_node([1, 3, 4]),
    ListNode.generate_node([2, 6]),
]))

ListNode.printof(x.mergeKLists3([
    ListNode.generate_node([]),
    ListNode.generate_node([])
]))