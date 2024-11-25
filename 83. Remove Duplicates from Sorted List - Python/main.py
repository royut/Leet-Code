# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def iter(self):
        here = self
        while here:
            print(here.val, end=" ")
            here = here.next
        print(" ")


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = head
        before = None
        set = {}
        while head:
            if head.val in set:
                before.next = head.next
                head = head.next
            else:
                set[head.val] = True
                before = head
                head = head.next

        return first


if __name__ == '__main__':
    print('in main')
    head = ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(1, ListNode(2))))))
    new = (Solution().deleteDuplicates(head))
    new.iter()