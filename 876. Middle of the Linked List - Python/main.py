# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def iter(self):
        here = self
        while here:
            print(here.val)
            here = here.next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        a = []
        while head:
            count += 1
            a.append(head)
            head = head.next

        return a[int(count / 2)]


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    # head.iter()
    print(Solution().middleNode(head))
