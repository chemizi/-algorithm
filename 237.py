# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def link(self, node):
        self.next = node


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        print("original linked list", end=": ")
        while node is not None:
            print(node.val, end=" ")
            node = node.next
        print()

        node = head
        linked_list_length = 1
        while node.next is not None:
            node = node.next
            linked_list_length += 1

        node_start = ListNode(None)
        node_start.next = head
        node = node_start
        for i in range(linked_list_length-n):
            node = node.next
        node.next = node.next.next

        node = node_start
        print("changed linked list", end=": ")
        while node.next is not None:
            print(node.next.val, end=" ")
            node = node.next
        print()

        return node_start.next


def main():
    head = ListNode(0)
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # head.link(node1)
    # node1.link(node2)
    # node2.link(node3)

    S = Solution()
    S.removeNthFromEnd(head, 1)


if __name__ == '__main__':
    main()
