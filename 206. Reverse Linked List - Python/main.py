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
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = []
        while head:
            a.append(head)
            head = head.next

        if len(a) > 0:
            reversed_head = ListNode()
            pointer = reversed_head
            for i in range(len(a) - 1, -1, -1):
                pointer.val = a[i].val
                if i != 0:
                    pointer.next = ListNode()
                    pointer = pointer.next

            return reversed_head
        return None


if __name__ == '__main__':
    print("in main")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    reverse = Solution().reverseList(None)
    reverse.iter()
