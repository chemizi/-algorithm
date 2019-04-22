# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def link(self, node):
        self.next = node


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def main():
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    head.link(node1)
    node1.link(node2)
    node2.link(node3)

    node = head
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()

    S = Solution()
    S.deleteNode(node2)

    node = head
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()


if __name__ == '__main__':
    main()
