__author__ = 'karenwu'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def traverseLinkedList(self,head):
        cur = head
        while cur != None:
            print cur.val,
            cur = cur.next
    @staticmethod
    def countNodes(head):
        count=0
        cur = head
        while cur!=None:
            count=count+1
            cur=cur.next
        return count


class Solution:
    def __init__(self):
        pass
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseLinkedList(self, head):
        """
        reverse the entire linked list
        """
        if head is None or head.next is None:
            return head

        pre = None
        cur = head
        next = None

        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    # n4 = ListNode(4)
    # n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    # n3.next = n4
    # n4.next = n5

    n1.traverseLinkedList(n1)
    print ListNode.countNodes(n1)
    s = Solution()
    # s.reverseBetween(n1,2,4)

    head = n1

    head = s.reverseLinkedList(head)
    n1.traverseLinkedList(head)
