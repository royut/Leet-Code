# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n1 = 0
        i = 1
        while l1:
            n1 = n1 + l1.val * i
            l1 = l1.next
            i *= 10
        n2 = 0
        i = 1
        while l2:
            n2 = n2 + l2.val * i
            l2 = l2.next
            i *= 10
        n = n1 + n2
        if n == 0:
            return ListNode(0)
        l = ListNode()
        current = l
        while n > 0:
            current.next = ListNode()
            current = current.next
            digit = n % 10
            n = n // 10
            current.val = digit
        current.next = None
        return l.next


if __name__ == '__main__':
    print('in main')
    num1 = ListNode(2, ListNode(4, ListNode(3)))
    num2 = ListNode(5, ListNode(6, ListNode(4)))
    num1 = ListNode(0)
    num2 = ListNode(0)
    l = (Solution().addTwoNumbers(num1, num2))

    while l:
        print(l.val)
        l = l.next