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
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        tempHead = head
        before = None
        current = head
        i = 0
        while current:
            print(i)
            i += 1
            if current.val == val:
                if not current.next:
                    if not before:
                        tempHead = None
                        current = current.next
                    else:
                        before.next = None
                        current = current.next
                else:
                    if not before:
                        tempHead = current.next
                        current = current.next
                    else:
                        before.next = current.next
                        current = current.next
            else:
                before = current
                current = current.next
        return tempHead


if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1))))))
    # head.iter()
    # new = Solution().removeElements(head, 1)
    # new.iter()
    new = Solution().removeElements(head, 1)
    new.iter()